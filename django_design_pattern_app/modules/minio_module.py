from injector import Module, singleton
from django_design_pattern_app.services.minio.minio import MinIOSDK
from minio import Minio
import os


class MinIOModule(Module):
    def configure(self, binder):
        minio_client = Minio(
            endpoint=os.getenv('MINIO_ENDPOINT'),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key=os.getenv('MINIO_SECRET_KEY'),
            secure=False
        )

        binder.bind(Minio, to=minio_client, scope=singleton)
        binder.bind(MinIOSDK, to=MinIOSDK, scope=singleton)
