import uuid
from functools import wraps
from typing import Callable, TypeVar, cast, Generic
from elasticsearch import Elasticsearch
from injector import inject
from pydantic import BaseModel
from typing import Dict, Optional, List, Any
from django_design_pattern_app.services.elasticsearch.indexing.users_index import UserIndexConfig
from django_design_pattern_app.services.redis.redis import RedisService

FuncT = TypeVar("FuncT", bound=Callable[..., Any])
ElasticPydanticModel = TypeVar("ElasticPydanticModel", bound=BaseModel)


class SearchELK(UserIndexConfig, Generic[ElasticPydanticModel]):

    @inject
    def __init__(self, es: Elasticsearch, redis: RedisService):
        """
        Initializes a SearchELK instance.

        :param es: The Elasticsearch client.
        :param redis: The Redis client.
        """
        self.es = es
        self.redis = redis

    @staticmethod
    def index_check_decorator(func: FuncT) -> FuncT:
        """
        A decorator that checks if the index exists, and creates it if it doesn't,
        before calling the decorated function.

        :param func: The function to decorate.
        :return: The decorated function.
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.check_index_exists():
                self.create_index()
            return func(self, *args, **kwargs)
        return cast(FuncT, wrapper)

    @property
    def read_name(self) -> str:
        """
        The name of the read alias for the index.

        The read alias is used for searching, and always points to the latest
        version of the index.

        :return: The name of the read alias for the index.
        """
        return self.es_index_name

    @property
    def write_name(self) -> str:
        """
        The name of the write alias for the index.

        The write alias is used for indexing and updating documents, and is
        switched to a new index name when the index is rotated.

        :return: The name of the write alias for the index.
        """
        return self.es_index_name + ".write"

    def get_new_index_name(self) -> str:
        """
        Generates a new index name that is ready to be created.

        This method generates a new index name by appending a uuid4
        to the index name. The new index name is then used as the
        target for the write alias.

        :return: A new index name, ready to be created.
        """
        guid = str(uuid.uuid4())
        return f"{self.es_index_name}_{guid}"

    def get_index_names_with_alias(self, alias) -> list[str]:
        """
        Returns a list of all index names that have the given alias.

        :param alias: The alias to search for.
        :return: A list of index names that have the given alias.
        """
        return list(self.es.indices.get_alias(name=alias).keys())

    def create_index(self):
        """
        Creates a new index, if it doesn't exist.

        Creates a new index with a unique name, and adds aliases to it for
        both the read and write aliases.

        Returns:
            dict: The result of the create operation
        """
        index_name = self.get_new_index_name()
        result = self.es.indices.create(index=index_name, mappings=self.es_index_mapping, settings=self.es_settings)
        self.es.indices.update_aliases(
            actions=[
                {"add": {"index": index_name, "alias": self.read_name}},
                {"add": {"index": index_name, "alias": self.write_name}},
            ]
        )
        return result

    def delete_index(self):
        """
        Deletes the index, if it exists.

        Returns:
            dict: The result of the delete operation
        """
        return self.es.indices.delete(index=self.write_name, ignore_unavailable=True)

    def check_index_exists(self):
        """
        Checks if the index exists.

        Returns:
            bool: `True` if the index exists, `False` otherwise.
        """
        return self.es.indices.exists(index=self.write_name)

    def refresh_index(self):
        """
        Refreshes the index to make the latest data searchable

        Returns:
            dict: The result of the refresh operation
        """
        return self.es.indices.refresh(index=self.write_name)

    @index_check_decorator
    def add(self, id: str, doc_data: ElasticPydanticModel):
        if not self.es.exists(index=self.write_name, id=id):
            return self.es.index(index=self.write_name, id=id, document=doc_data.dict(), refresh=True)

    @index_check_decorator
    def remove(self, id):
        """
        Removes a document from the index by its id.

        Args:
            id: The id of the document to remove.

        Returns:
            The result of the remove operation.
        """
        if self.es.exists(index=self.write_name, id=id):
            return self.es.delete(index=self.write_name, id=id, refresh=True)

    @index_check_decorator
    def get(self, id) -> ElasticPydanticModel | None:
        """
        Get a document from the index by its id.

        Args:
            id: The id of the document to retrieve.

        Returns:
            The document as a pydantic model, or None if it doesn't exist.
        """
        res = self.es.get(index=self.read_name, id=id)["_source"]
        if res:
            return self.pydantic_model.parse_obj(res)
        return None


    @index_check_decorator
    def update(self, id, doc_data: ElasticPydanticModel):
        """
        Update the document with the given id in the index with the given data

        Args:
            id (str): The id of the document to update
            doc_data (ElasticPydanticModel): The data to update in the document

        Returns:
            dict: The result of the update
        """
        return self.es.update(index=self.write_name, id=id, doc=doc_data.dict(), refresh=True, doc_as_upsert=True)

    @index_check_decorator
    def search(self, query: dict | None = None, size: int | None = None, suggest: dict | None = None,
               aggs: dict | None = None):
        """
        Search in the index with the given query, suggestion, size and aggregation

        Args:
            query (dict | None): The query to search in the index
            size (int | None): The size of the result
            suggest (dict | None): The suggestion to search in the index
            aggs (dict | None): The aggregation to perform on the result

        Returns:
            dict: The result of the search
        """
        return self.es.search(index=self.read_name, query=query, suggest=suggest, size=size, aggs=aggs)

    @index_check_decorator
    def new_search(
            self,
            query: Optional[Dict[str, Any]] = None,
            size: Optional[int] = None,
            suggest: Optional[Dict[str, Any]] = None,
            aggs: Optional[Dict[str, Any]] = None,
            source_includes: Optional[List[str]] = None,
            source_excludes: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        A wrapper around Elasticsearch's search API.

        :param query: The query to filter the search results.
        :param size: The number of results to return.
        :param suggest: The suggest query.
        :param aggs: The aggregation query.
        :param source_includes: The fields to include in the _source field.
        :param source_excludes: The fields to exclude from the _source field.
        :return: The search result.
        """
        body = {}
        if query:
            body['query'] = query
        if size is not None:
            body['size'] = size
        if aggs:
            body['aggs'] = aggs
        if suggest:
            body['suggest'] = suggest
        if source_includes is not None or source_excludes is not None:
            body['_source'] = {}
            if source_includes is not None:
                body['_source']['includes'] = source_includes
            if source_excludes is not None:
                body['_source']['excludes'] = source_excludes

        return self.es.search(index=self.read_name, body=body)



