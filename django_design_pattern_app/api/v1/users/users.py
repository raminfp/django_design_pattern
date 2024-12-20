from rest_framework import generics
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from django_design_pattern_app.injector.base_injector import BaseInjector
from django_design_pattern_app.middleware.exceptions import handle_exceptions
from django_design_pattern_app.middleware.validate import validate_serializer
from django_design_pattern_app.repositories.users_repo import UsersRepo
from django_design_pattern_app.middleware.response import APIResponse
from django_design_pattern_app.permissions import permissions
from django_design_pattern_app.permissions.permissions import IsSuperUser


class BaseView(APIView, AutoSchema):
    user_repo = BaseInjector.get(UsersRepo)


class IndexView(BaseView, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated, IsSuperUser)
    # serializer_class = UserInfoUpdateSerializer

    @validate_serializer()
    @handle_exceptions
    def get(self, request):

        """
        This is a test view, which is used to test the health of other services.
        It calls the database, minio, and elasticsearch.
        """
        print("Starting... Call  database  ")
        self.user_repo.get_user_by_id(request.user.id)
        print("Starting... Call minio ")
        self.user_repo.minio_find()
        print("Starting... Call elasticsearch ")
        self.user_repo.elk_search()
        return APIResponse(data=True)
