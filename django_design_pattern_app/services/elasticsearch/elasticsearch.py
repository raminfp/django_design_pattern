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
        self.es = es
        self.redis = redis

    @staticmethod
    def index_check_decorator(func: FuncT) -> FuncT:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self.check_index_exists():
                self.create_index()
            return func(self, *args, **kwargs)
        return cast(FuncT, wrapper)

    @property
    def read_name(self) -> str:
        return self.es_index_name

    @property
    def write_name(self) -> str:
        return self.es_index_name + ".write"

    def get_new_index_name(self):
        guid = str(uuid.uuid4())
        return f"{self.es_index_name}_{guid}"

    def get_index_names_with_alias(self, alias) -> list[str]:
        return list(self.es.indices.get_alias(name=alias).keys())

    def create_index(self):
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
        return self.es.indices.delete(index=self.write_name, ignore_unavailable=True)

    def check_index_exists(self):
        return self.es.indices.exists(index=self.write_name)

    def refresh_index(self):
        return self.es.indices.refresh(index=self.write_name)

    @index_check_decorator
    def add(self, id: str, doc_data: ElasticPydanticModel):
        if not self.es.exists(index=self.write_name, id=id):
            return self.es.index(index=self.write_name, id=id, document=doc_data.dict(), refresh=True)

    @index_check_decorator
    def remove(self, id):
        if self.es.exists(index=self.write_name, id=id):
            return self.es.delete(index=self.write_name, id=id, refresh=True)

    @index_check_decorator
    def get(self, id) -> ElasticPydanticModel | None:
        res = self.es.get(index=self.read_name, id=id)["_source"]
        if res:
            return self.pydantic_model.parse_obj(res)
        return None

    @index_check_decorator
    def update(self, id, doc_data: ElasticPydanticModel):
        return self.es.update(index=self.write_name, id=id, doc=doc_data.dict(), refresh=True, doc_as_upsert=True)

    @index_check_decorator
    def search(self, query: dict | None = None, size: int | None = None, suggest: dict | None = None,
               aggs: dict | None = None):
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



