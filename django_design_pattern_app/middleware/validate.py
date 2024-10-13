from functools import wraps
from ngr_update_system_app.utils.validations import ValidateAndHandleErrors


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
