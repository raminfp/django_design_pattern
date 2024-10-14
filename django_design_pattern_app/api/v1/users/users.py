from rest_framework import generics
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from sentry_sdk import capture_exception
from django_design_pattern_app.injector.base_injector import BaseInjector
from django_design_pattern_app.middleware.exceptions import handle_exceptions
from django_design_pattern_app.middleware.validate import validate_serializer
from django_design_pattern_app.permissions import permissions
from django_design_pattern_app.permissions.permissions import IsSuperUser
from django_design_pattern_app.repositories.users_repo import UsersRepo
from django_design_pattern_app.middleware.response import APIResponse
from django_design_pattern_app.utils.validations import ValidateAndHandleErrors


class BaseView(APIView, AutoSchema):
    user_repo = BaseInjector.get(UsersRepo)


class IndexView(BaseView, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated, IsSuperUser)
    # serializer_class = UserInfoUpdateSerializer

    @validate_serializer()
    @handle_exceptions
    def get(self, request):
        """
        Update user information
        """
        print("Starting")
        self.user_repo.test_elk()
        print("User information")
        sz = self.get_serializer(data=request.data)
        result = ValidateAndHandleErrors.validate_and_handle_errors(sz)
        if result:
            return result
        # TODO : ...
        return APIResponse(data=True)
