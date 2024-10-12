from django.urls import path
# from django_design_pattern_app.api.v1.auth.auth import (
#     LogoutView,
#     LoginView
# )
from django_design_pattern_app.api.v1.users.users import (
 IndexView
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


user_url = [

    # path('user/login', LoginView.as_view(), name="user_login"),
    # path('user/logout', LogoutView.as_view(), name="user_logout"),

    # path('user/info', UserUpdateInfoView.as_view(), name="userupdateinfo"),
    # path('user/me', UserGetInfoView.as_view(), name="usergetinfo"),
    # path('user/userdeviceinfo', UserInfoDeviceView.as_view(), name="userdeviceinfo"),
    path('index', IndexView.as_view(), name='index'),
    path('update', IndexView.as_view(), name='update'),

]