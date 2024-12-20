from elasticsearch import Elasticsearch
from injector import inject
from django_design_pattern_app.services.redis.redis import RedisService
from django_design_pattern_app.services.minio.minio import MinioSDK
from django_design_pattern_app.services.elasticsearch.elasticsearch import SearchELK


class BaseRepo:

    @inject
    def __init__(self, minio_sdk: MinioSDK, elk: SearchELK):
        """
        Constructor for BaseRepo.

        Parameters
        ----------
        minio_sdk : MinIOSDK
            MinIO service object
        elk : SearchELK
            Elasticsearch service object
        """
        self.service_minio = minio_sdk
        self.elk = elk
