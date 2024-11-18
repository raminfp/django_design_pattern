from django.http import JsonResponse
from django_design_pattern_app.utils.messages import ErrorMessage, SuccessMessage


class APIResponse(JsonResponse):
    def __init__(self, data=None, error_code=None, status=None, success_code=None, content_type='application/json'):
        """
        Args:
            data: The data to be returned in the response body.
            error_code (int): The error code to be returned in the response body.
            status (int): The HTTP status code to use for the response.
            success_code (int): The success code to be returned in the response body.
            content_type (str): The content type to use for the response.

        Returns:
            APIResponse: The API response object.
        """
        content = {'error': {}, "success": {}, 'data': data}
        if error_code:
            content['error'] = {'code': error_code, 'description': ErrorMessage.errors[error_code]}
        if success_code:
            content['success'] = {'code': success_code, 'description': SuccessMessage.success[success_code]}
        super().__init__(content, status=status, content_type=content_type)
