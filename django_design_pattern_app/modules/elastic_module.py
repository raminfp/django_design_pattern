from injector import Module, singleton, provider
from elasticsearch import Elasticsearch
from redis import Redis
from django.conf import settings


class ElasticModule(Module):
    @singleton
    @provider
    def provide_elasticsearch(self) -> Elasticsearch:
        return Elasticsearch(settings.ELASTICSEARCH_DSL['default']['hosts'])

    @singleton
    @provider
    def provide_redis(self) -> Redis:
        return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def configure_elastic(binder):
    binder.bind(Elasticsearch, to=Elasticsearch, scope=singleton)
    binder.bind(Redis, to=Redis, scope=singleton)
