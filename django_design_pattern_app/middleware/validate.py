from functools import wraps
from django_design_pattern_app.utils.validations import ValidateAndHandleErrors


def validate_serializer():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            result = ValidateAndHandleErrors.validate_and_handle_errors(serializer)
            if result:
                return result
            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator


def validate_serializer_zip():
    """
    A decorator that validates a serializer for both GET and POST requests.

    Works just like `validate_serializer`, but also supports GET requests.

    :param view_func: The view function to decorate
    :type view_func: function
    :return: The result of the view function
    :rtype: object
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            if request.method == 'GET':
                data = request.GET
            else:
                data = request.data
            serializer = self.get_serializer(data=data)
            result = ValidateAndHandleErrors.validate_and_handle_errors(serializer)
            if result:
                return result
            request.serializer_context = serializer.context
            return view_func(self, request, *args, **kwargs)

        return wrapper

    return decorator
