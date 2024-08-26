from injector import Module, singleton, provider
import pika
from django.conf import settings
from django_design_pattern_app.services.rabbitmq.rabbitmq import RabbitMQService

'''docs
# Obtain an instance of RabbitMQService from the injector
rabbitmq_service = BaseInjector.get(RabbitMQService)

# Example usage
rabbitmq_service.declare_queue('my_queue')
rabbitmq_service.publish_message('my_exchange', 'my_routing_key', 'Hello, RabbitMQ!')

'''


class RabbitMQModule(Module):
    @singleton
    @provider
    def provide_rabbitmq_connection(self) -> pika.BlockingConnection:
        parameters = pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            virtual_host=settings.RABBITMQ_VIRTUAL_HOST,
            credentials=pika.PlainCredentials(
                username=settings.RABBITMQ_USERNAME,
                password=settings.RABBITMQ_PASSWORD
            )
        )
        return pika.BlockingConnection(parameters)

    @singleton
    @provider
    def provide_rabbitmq_service(self, connection: pika.BlockingConnection) -> RabbitMQService:
        return RabbitMQService(connection)
