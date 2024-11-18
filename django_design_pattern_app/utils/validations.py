from rest_framework.exceptions import ErrorDetail
from rest_framework.views import APIView
from django_design_pattern_app.middleware.response import APIResponse


class ValidateAndHandleErrors(APIView):

    @staticmethod
    def validate_and_handle_errors(serializer):
        """
        Validates the given serializer and returns an APIResponse object based on the errors
        in the serializer. If there are no errors, returns None.

        The APIResponse object is created using the error code and status code from the
        error messages in the serializer.

        The following error codes are used:
        1004: Blank
        1006: Max length
        1000: Invalid
        1007: Unique
        1008: Password mismatch
        1009: Invalid choice
        1010: Min length
        1011: Invalid image
        1012: Mobile value
        1013: Mobile length
        1014: Sms code send
        1015: Code wrong
        1016: Time wrong
        1017: Package invalid
        1018: Customer invalid
        1019: Arch invalid
        1021: Invalid mobile
        1030: Empty

        If the error is not found in the above list, a generic error message with code 1 is returned.

        :param serializer: The serializer to validate
        :type serializer: rest_framework.serializers.Serializer
        :return: An APIResponse object with the error code and status code
        :rtype: APIResponse
        """
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
