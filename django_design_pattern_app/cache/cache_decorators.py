from django.core.cache import cache
import json


class Cache(object):

    def create_cache(self, object_name, pydantic_model):
        """
        Cache the result of a function call in Django's cache framework.

        The cache key is a combination of the object name and the object id.
        The cache expiration is set to 1 hour.

        :param func: The function to cache.
        :return: The cached result if it exists, otherwise the result of func.
        """
        def decorator(func):
            """
            Cache the result of a function call in Django's cache framework.

            The cache key is a combination of the object name and the object id.
            The cache expiration is set to 1 hour.

            :param func: The function to cache.
            :return: The cached result if it exists, otherwise the result of func.
            """
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
            """
            Invalidate the cache for a given object and id.

            :param func: The view function to decorate
            :type func: function
            :param object_name: The name of the object to be cached
            :type object_name: str
            :param object_id: The id of the object to be cached
            :type object_id: str
            :param args: The args to be passed to the view function
            :type args: tuple
            :param kwargs: The kwargs to be passed to the view function
            :type kwargs: dict
            :return: The result of the view function
            :rtype: object
            """
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
