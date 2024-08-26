from django.core.cache import cache
import json


class Cache(object):

    def create_cache(self, object_name, pydantic_model):
        def decorator(func):
            def wrapper(*args, **kwargs):
                object_id = kwargs.get('id') or args[0]
                key_name = f"{object_name}_{object_id}"
                cached_data = cache.get(key_name)
                if cached_data:
                    # logger.info(f"Cache HIT for {key_name}")
                    return pydantic_model(**json.loads(cached_data))
                # logger.info(f"Cache MISS for {key_name}")
                result = func(*args, **kwargs)
                # TODO - use Redis
                cache.set(key_name, json.dumps(result.dict()), timeout=3600)  # Cache for 1 hour
                return result
            return wrapper
        return decorator

    def invalidate_cache(self, object_name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                object_id = kwargs.get('id') or args[0]
                key_name = f"{object_name}_{object_id}"
                result = func(*args, **kwargs)
                # TODO - use Redis
                cache.delete(key_name)
                cache.set(key_name, json.dumps(result.dict()), timeout=3600)
                return result
            return wrapper
        return decorator
