from rest_framework import serializers


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
