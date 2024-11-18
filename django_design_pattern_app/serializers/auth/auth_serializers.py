from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.text import gettext_lazy as _


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        """
        Check the serializer is valid.

        Store the token in the instance so it can be used later.
        """
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        """
        Save the object, blacklisting the given refresh token.

        :raises serializers.ValidationError: if the token is invalid or expired
        """
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            self.fail('bad_token')


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

        # Optionally, you can add additional validation for the refresh token here
    def validate_refresh(self, value):
        """
        Optionally, you can add additional validation for the refresh token here

        :param value: The refresh token to validate
        :type value: str
        :return: The validated refresh token
        :rtype: str
        """
        return value


class DeviceArrayField(serializers.ListField):
    def to_internal_value(self, data):

        """
        Validate the given data as a list of strings.

        :param data: The data to validate
        :type data: list or str
        :raises serializers.ValidationError: If the given data is invalid
        :return: The validated list of strings
        :rtype: list
        """
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


