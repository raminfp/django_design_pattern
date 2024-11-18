from functools import wraps
from sentry_sdk import capture_exception
from django_design_pattern_app.middleware.response import APIResponse

'''
  @handle_exceptions
  def post(self, request):
        pass
'''


def handle_exceptions(func):
    """
    A decorator that catches all exceptions in a view and sends them to
    Sentry before returning a 500 response.

    Example usage:

    @handle_exceptions
    def post(self, request):
        pass
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            capture_exception(e)
            return APIResponse(error_code=1, status=500)

    return wrapper


def handle_exceptions_special(*exception_handlers):
    """
    A decorator that catches exceptions in a view and sends them to Sentry before returning a 500 response.

    It allows you to specify special exception handlers for specific exceptions.

    Example usage:

    @handle_exceptions_special(
        (FileNotFoundError, 1111, 404),
        (IOError, 4, 500),
    )
    def post(self, request):
        pass

    This decorator will catch `FileNotFoundError` and `IOError` and return a 404 and 500 response respectively, while catching all other exceptions and returning a 500 response.

    :param exception_handlers: A list of tuples in the form of `(exception_type, error_code, status)`.
    :type exception_handlers: list
    :return: A decorator that will catch exceptions and return a 500 response.
    :rtype: function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for exception_type, error_code, status in exception_handlers:
                    if isinstance(e, exception_type):
                        capture_exception(e)
                        return APIResponse(error_code=error_code, status=status)
                # Default exception handling
                capture_exception(e)
                return APIResponse(error_code=1, status=500)

        return wrapper

    return decorator
