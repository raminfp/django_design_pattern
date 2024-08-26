from injector import Injector
from django_design_pattern_app.modules.elastic_module import ElasticModule
from django_design_pattern_app.modules.minio_module import MinIOModule
from django_design_pattern_app.modules.redis_module import RedisModule
from django_design_pattern_app.modules.rabbitmq_module import RabbitMQModule
from django_design_pattern_app.modules.kavenegar_module import KavenegarModule
import os

BaseInjector = Injector(
    [
        ElasticModule,
        MinIOModule,
        RedisModule,
        RabbitMQModule,
        KavenegarModule(os.getenv('KAVENEGAR_KEY'))

    ]
)
