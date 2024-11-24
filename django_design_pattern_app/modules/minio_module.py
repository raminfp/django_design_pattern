from injector import Module, singleton
from django_design_pattern_app.services.minio.minio import MinioSDK
from minio import Minio
import os


class MinIOModule(Module):
    def configure(self, binder):
        """
        Binds MinIO SDK to the injector. This allows the MinIOSDK class to be
        injected into other classes.

        :param binder: The injector's binder
        :type binder: injector.Binder
        :return: None
        :rtype: None
        """
        minio_client = Minio(
            endpoint=os.getenv('MINIO_ENDPOINT'),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key=os.getenv('MINIO_SECRET_KEY'),
            secure=False
        )

        binder.bind(Minio, to=minio_client, scope=singleton)
        binder.bind(MinioSDK, to=MinioSDK, scope=singleton)
