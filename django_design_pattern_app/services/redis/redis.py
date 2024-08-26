from redis import Redis
from injector import inject, singleton
import time

@singleton
class RedisService:
    @inject
    def __init__(self, redis: Redis):
        self.redis = redis

    def sadd(self, name: str, *values):
        """Add members to a set."""
        return self.redis.sadd(name, *values)

    def set(self, name: str, value: str):
        """Set the value of a key."""
        return self.redis.set(name, value)

    def get(self, name: str):
        """Get the value of a key."""
        return self.redis.get(name)

    def sinter(self, *names):
        """Intersect multiple sets."""
        return self.redis.sinter(*names)

    def sismember(self, name: str, value: str):
        """Check if a value is a member of a set."""
        return self.redis.sismember(name, value)

    '''
        Usage : 
        user_id = 'user_123'
        rate_limit = 10  # Allow 10 requests
        time_period = 60  # Per 60 seconds
        rate_limiter_service.is_rate_limited(user_id, rate_limit, time_period)

    '''
    def is_rate_limited(self, key: str, limit: int, period: int) -> bool:
        """
        Check if the rate limit has been exceeded.

        :param key: The unique key for the rate limiter (e.g., user ID or IP address).
        :param limit: The maximum number of allowed requests.
        :param period: The time period in seconds.
        :return: True if rate limited, False otherwise.
        """
        # Use a Redis pipeline to perform atomic operations
        with self.redis.pipeline() as pipe:
            pipe.incr(key)
            pipe.expire(key, period)
            count, _ = pipe.execute()

        # Check if the request count exceeds the limit
        return count > limit