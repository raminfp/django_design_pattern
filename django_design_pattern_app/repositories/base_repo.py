from elasticsearch import Elasticsearch
from injector import inject
from django_design_pattern_app.services.redis.redis import RedisService
from django_design_pattern_app.services.minio.minio import MinIOSDK
from django_design_pattern_app.services.elasticsearch.elasticsearch import SearchELK


class BaseRepo:

    @inject
    def __init__(self, minio_sdk: MinIOSDK, elk: SearchELK):
        self.service_minio = minio_sdk
        self.elk = elk
