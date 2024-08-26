from rest_framework import serializers
import re
from ngr_diag_isaco_app.models import Representations, SerialNumberDevice


class AdminLoginSerializer(serializers.Serializer):
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

    # def validate_mobile(self, value):
    #     if value is not None:
    #         phone_number_pattern = re.compile(r'^\d{11}$')  # Adjust the pattern as needed
    #         if not phone_number_pattern.match(value):
    #             raise serializers.ValidationError(detail='Invalid phone number format.', code="invalid_mobile")
    #     return value


class ListOfAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Representations
        fields = ['id', 'work_phone', 'city', 'state', 'agency_code', 'agency_name', 'address', 'is_active', 'username']


class ListOfDeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
        error_messages={
            'null': 'Username cannot be null.',
            'invalid': 'Invalid username.'
        }
    )
    class Meta:
        model = SerialNumberDevice
        fields = ['id', 'is_active', 'agency_id', 'serial_number']


class StatusDeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
        error_messages={
            'null': 'Username cannot be null.',
            'invalid': 'Invalid username.'
        }
    )
    is_active = serializers.BooleanField(
        required=False
    )

class DeleteDeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        allow_null=True,
        required=False,
        error_messages={
            'null': 'Username cannot be null.',
            'invalid': 'Invalid username.'
        }
    )

class AddDeviceSerializer(serializers.Serializer):
    pass
