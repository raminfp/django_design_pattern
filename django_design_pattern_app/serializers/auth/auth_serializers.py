from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.text import gettext_lazy as _


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            self.fail('bad_token')


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate_refresh(self, value):
        # Optionally, you can add additional validation for the refresh token here
        return value


class DeviceArrayField(serializers.ListField):
    def to_internal_value(self, data):

        if not isinstance(data, list):
            raise serializers.ValidationError(detail="is not list", code="invalid")
        else:
            if len(data) == 0:
                raise serializers.ValidationError(detail="list is empty", code="blank")
        for item in data:
            if not isinstance(item, str):
                raise serializers.ValidationError(detail="not string", code="invalid")
            if not item:
                raise serializers.ValidationError(detail="is empty", code="blank")

        return super().to_internal_value(data)


