from functools import wraps
from sentry_sdk import capture_exception
from django_design_pattern_app.middleware.response import APIResponse

'''
  @handle_exceptions
  def post(self, request):
        pass
'''


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            capture_exception(e)
            return APIResponse(error_code=1, status=500)

    return wrapper


'''
  @handle_exceptions_special(
        (FileNotFoundError, 1111, 404),
        (IOError, 4, 500),
    )
  def post(self, request):
        pass
'''


def handle_exceptions_special(*exception_handlers):
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
