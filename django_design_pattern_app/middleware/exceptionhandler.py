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
    """
    Custom exception handler for Django REST framework. It's used to handle any
    unhandled exceptions in the application and return a response with the
    appropriate status code and error message.

    The handler takes an exception object and a context dictionary as parameters.
    It uses the exception object to determine the type of error and looks up the
    appropriate response handler in the `handlers` dictionary. If the exception
    type is found, the handler is called with the exception object, context
    dictionary, and any response object as parameters. The handler should return
    a response object with the appropriate status code and error message.

    If the exception type is not found in the `handlers` dictionary, the handler
    returns the original response object, if any.

    Parameters:
        exc (Exception): The exception object
        context (dict): The context dictionary

    Returns:
        response (Response): The response object
    """
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
    """
    Handle ParseError exceptions raised by rest_framework.parsers.JSONParser.

    This function is called when a ParseError exception is raised by
    rest_framework.parsers.JSONParser. It returns a response object with a
    status code of 400 and an error message indicating that the JSON data
    is malformed.

    Parameters:
        exc (Exception): The ParseError exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The response object
    """
    response.data = create_error_json(1234, "ساختار JSON  درست نمی باشد", "")
    return response


def _handle_permissiondenied_error(exc, context, response):
    """
    Handle PermissionDenied exceptions raised by rest_framework.permissions.

    This function is called when a PermissionDenied exception is raised by
    rest_framework.permissions. It returns a response object with a status
    code of 403 and an error message indicating that the user does not have
    permission to access the requested resource.

    Parameters:
        exc (Exception): The PermissionDenied exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The response object
    """
    response.data = create_error_json(2342, "دسترسی شما غیرمجاز می باشد", "")
    return response


def _handle_simple_jwt_auth_error(exc, context, response):
    """
    Handle InvalidToken exceptions raised by rest_framework_simplejwt.authentication.JWTAuthentication.

    This function is called when an InvalidToken exception is raised by
    rest_framework_simplejwt.authentication.JWTAuthentication. It returns a
    response object with a status code of 401 and an error message indicating
    that the JWT token is invalid.

    Parameters:
        exc (Exception): The InvalidToken exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The response object
    """
    response.data = create_error_json(1543, "توکن JWT نادرست می باشد", "")
    return response


def _handle_authentication_error(exc, context, response):
    """
    Handle NotAuthenticated exceptions raised by rest_framework.authentication.

    This function is called when a NotAuthenticated exception is raised by
    rest_framework.authentication. It returns a response object with a status
    code of 401 and an error message indicating that authentication failed.

    Parameters:
        exc (Exception): The NotAuthenticated exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The response object
    """
    response.data = create_error_json(9876, "احراز هویت به درستی انجام نشد لظفا مجدد ورود کنید", "")
    return response


def _handle_exception_error(exc, context, response):
    """
    Handle all other exceptions raised by the application.

    This function is called when any other exception is raised by the
    application. It returns a response object with a status code of 500 and
    an error message indicating that an unknown error occurred.

    Parameters:
        exc (Exception): The exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The response object
    """
    response.data = create_error_json(9876, "خطای نامشخص رخ داده است", "")
    return response


def _handle_http500_error(exc, context, response):
    """
    Handle Http500 exceptions raised by Django.

    This function is called when an Http500 exception is raised by Django.
    It returns the original response object.

    Parameters:
        exc (Exception): The Http500 exception object
        context (dict): The context dictionary
        response (Response): The response object

    Returns:
        response (Response): The original response object
    """
    return response
