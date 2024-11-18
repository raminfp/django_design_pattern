from django.urls import path

from django_design_pattern_app.api.v1.users.users import (
 IndexView
)


user_url = [

    path('index', IndexView.as_view(), name='index'),
    path('update', IndexView.as_view(), name='update'),

]