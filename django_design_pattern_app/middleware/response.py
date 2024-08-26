from django.http import JsonResponse
from django_design_pattern_app.utils.messages import ErrorMessage


class APIResponse(JsonResponse):
    def __init__(self, data=None, error_code=None, status=None, content_type='application/json'):
        content = {'error': {}, 'data': data}
        if error_code:
            content['error'] = {'code': error_code, 'description': ErrorMessage.errors[error_code]}
        super().__init__(content, status=status, content_type=content_type)

