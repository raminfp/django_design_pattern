from rest_framework import serializers
from django_design_pattern_app.models.users import Users


class UserInfoUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        # allow_blank=True,
        max_length=100,
        error_messages={
            'required': 'Please provide your last name.',
            'blank': 'Last name should not be blank.',
            'max_length': 'message length is larger'
        }
    )

    last_name = serializers.CharField(
        # allow_blank=True,
        max_length=100,
        error_messages={
            'required': 'Please provide your last name.',
            'blank': 'Last name should not be blank.',
            'max_length': 'message length is larger'
        }
    )

    job = serializers.CharField(
        # allow_blank=True,
        max_length=100,
        error_messages={
            'required': 'Please provide your job title.',
            'blank': 'Job title should not be blank.',
            'max_length': 'message length is larger'
        }
    )

    state = serializers.CharField(
        # allow_blank=True,
        max_length=100,
        error_messages={
            'required': 'Please select your province.',
            'blank': 'Province should not be blank.',
            'max_length': 'message length is larger'
        }
    )

    city = serializers.CharField(
        # allow_blank=True,
        max_length=100,
        error_messages={
            'required': 'Please provide your city.',
            'blank': 'City should not be blank.',
            'max_length': 'message length is larger'
        }
    )

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'state', 'city']


class UserGetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'state', 'city']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        allow_null=True,
        required=False,
        error_messages={
            'null': 'Username cannot be null.',
            'invalid': 'Invalid username.'
        }
    )

    password = serializers.CharField(
        allow_null=True,
        required=False,
        error_messages={
            'null': 'Password cannot be null.',
            'invalid': 'Invalid password.',
        }
    )


class ResLoginSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=1000)
    refresh_token = serializers.CharField()
    is_new_user = serializers.BooleanField()
