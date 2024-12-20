import os

from injector import Module, singleton, provider
from elasticsearch import Elasticsearch
from redis import Redis
from django.conf import settings


class ElasticModule(Module):
    @singleton
    @provider
    def provide_elasticsearch(self) -> Elasticsearch:
        """
        Provides an instance of Elasticsearch

        Returns:
            Elasticsearch: An instance of Elasticsearch
        """
        return Elasticsearch(os.getenv('ELASTICSEARCH_HOSTS'))

    @singleton
    @provider
    def provide_redis(self) -> Redis:
        """
        Provides an instance of Redis

        Returns:
            Redis: An instance of Redis
        """
        return Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))


def configure_elastic(binder):
    """
    Configures the injector for Elasticsearch and Redis

    Args:
        binder: The injector's binder
    """
    binder.bind(Elasticsearch, to=Elasticsearch, scope=singleton)
    binder.bind(Redis, to=Redis, scope=singleton)
