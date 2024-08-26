from rest_framework.exceptions import ErrorDetail
from rest_framework.views import APIView
from django_design_pattern_app.middleware.response import APIResponse


class ValidateAndHandleErrors(APIView):

    @staticmethod
    def validate_and_handle_errors(serializer):
        serializer.is_valid()
        if serializer.errors:
            for key, value in serializer.errors.items():
                if isinstance(value, list):
                    for error_detail in value:
                        if isinstance(error_detail, ErrorDetail):
                            if error_detail.code == 'blank':
                                return APIResponse(data="", error_code=1004, status=404)
                            if error_detail.code == 'max_length':
                                return APIResponse(data="", error_code=1006, status=404)
                            if error_detail.code == 'required':
                                return APIResponse(data="", error_code=1004, status=404)
                            if error_detail.code == 'invalid':
                                return APIResponse(data="", error_code=1000, status=404)
                            if error_detail.code == 'unique':
                                return APIResponse(data="", error_code=1007, status=404)
                            if error_detail.code == 'password_mismatch':
                                return APIResponse(data="", error_code=1008, status=404)
                            if error_detail.code == 'invalid_choice':
                                return APIResponse(data="", error_code=1009, status=404)
                            if error_detail.code == 'min_length':
                                return APIResponse(data="", error_code=1010, status=404)
                            if error_detail.code == 'invalid_image':
                                return APIResponse(data="", error_code=1011, status=404)
                            if error_detail.code == 'max_value':
                                return APIResponse(data="", error_code=1006, status=404)
                            if error_detail.code == 'min_value':
                                return APIResponse(data="", error_code=1010, status=404)
                            if error_detail.code == 'mobile_length':
                                return APIResponse(data="", error_code=1013, status=404)
                            if error_detail.code == 'mobile_value':
                                return APIResponse(data="", error_code=1012, status=404)
                            if error_detail.code == 'sms_code_send':
                                return APIResponse(data="", error_code=1014, status=404)
                            if error_detail.code == 'code_wrong':
                                return APIResponse(data="", error_code=1015, status=404)
                            if error_detail.code == 'time_wrong':
                                return APIResponse(data="", error_code=1016, status=404)
                            if error_detail.code == 'package_invalid':
                                return APIResponse(data="", error_code=1017, status=404)
                            if error_detail.code == 'customer_invalid':
                                return APIResponse(data="", error_code=1018, status=404)
                            if error_detail.code == 'arch_invalid':
                                return APIResponse(data="", error_code=1019, status=404)
                            if error_detail.code == 'null':
                                return APIResponse(data="", error_code=1004, status=404)
                            if error_detail.code == 'invalid_mobile':
                                return APIResponse(data="", error_code=1021, status=404)
                            if error_detail.code == 'empty':
                                return APIResponse(data="", error_code=1030, status=404)

                return APIResponse(data="", error_code=1, status=500)

        return None
