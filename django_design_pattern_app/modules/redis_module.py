from injector import Module, singleton, provider
from redis import Redis
from django.conf import settings


class RedisModule(Module):
    @singleton
    @provider
    def provide_redis(self) -> Redis:
        """
        Provides an instance of Redis

        Returns:
            Redis: An instance of Redis
        """
        return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def configure_elastic(binder):
    """
    Configures the injector for Redis

    Args:
        binder: The injector's binder
    """
    binder.bind(Redis, to=Redis, scope=singleton)
