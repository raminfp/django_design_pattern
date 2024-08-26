from rest_framework.views import exception_handler


def create_error_json(code, message, data):
    return {
        "data": data,
        "error": {
            "code": code,
            "description": message
        }
    }


def custom_exception_handler(exc, context):
    handlers = {
        'Exception': _handle_exception_error,
        'PermissionDenied': _handle_permissiondenied_error,
        'NotAuthenticated': _handle_authentication_error,
        'ParseError': _handle_json_parser_error,
        'InvalidToken': _handle_simple_jwt_auth_error,
    }

    response = exception_handler(exc, context)
    if response:
        response.data['status_code'] = response.status_code
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_json_parser_error(exc, context, response):
    response.data = create_error_json(1234, "ساختار JSON  درست نمی باشد", "")
    return response


def _handle_permissiondenied_error(exc, context, response):
    response.data = create_error_json(2342, "دسترسی شما غیرمجاز می باشد", "")
    return response


def _handle_simple_jwt_auth_error(exc, context, response):
    response.data = create_error_json(1543, "توکن JWT نادرست می باشد", "")
    return response


def _handle_authentication_error(exc, context, response):
    response.data = create_error_json(9876, "احراز هویت به درستی انجام نشد لظفا مجدد ورود کنید", "")
    return response


def _handle_exception_error(exc, context, response):
    response.data = create_error_json(9876, "خطای نامشخص رخ داده است", "")
    return response


def _handle_http500_error(exc, context, response):
    return response
