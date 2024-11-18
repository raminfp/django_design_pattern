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
        """
        Provides a singleton instance of `pika.BlockingConnection` for interacting
        with a RabbitMQ broker. The connection parameters are derived from Django
        settings `RABBITMQ_HOST`, `RABBITMQ_PORT`, `RABBITMQ_VIRTUAL_HOST`,
        `RABBITMQ_USERNAME`, and `RABBITMQ_PASSWORD`.
        """
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
        """
        Provides a singleton instance of `RabbitMQService` for interacting
        with the RabbitMQ broker.

        The instance is initialized with the provided `connection` and is
        the primary interface for interacting with the RabbitMQ broker.

        :param connection: A `pika.BlockingConnection` instance
        :return: An instance of `RabbitMQService`
        """
        return RabbitMQService(connection)
