from injector import Module, singleton, provider
from redis import Redis
from django.conf import settings


class RedisModule(Module):
    @singleton
    @provider
    def provide_redis(self) -> Redis:
        return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def configure_elastic(binder):
    binder.bind(Redis, to=Redis, scope=singleton)
