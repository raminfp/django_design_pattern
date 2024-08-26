import pika
from injector import inject, singleton


@singleton
class RabbitMQService:
    @inject
    def __init__(self, connection: pika.BlockingConnection):
        self.connection = connection
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name: str):
        """Declare a queue."""
        self.channel.queue_declare(queue=queue_name)

    def publish_message(self, exchange: str, routing_key: str, body: str):
        """Publish a message to an exchange."""
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=body)

    def consume_messages(self, queue_name: str, callback):
        """Start consuming messages from a queue."""
        self.channel.basic_consume(queue=queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        self.channel.start_consuming()

    def close_connection(self):
        """Close the RabbitMQ connection."""
        self.connection.close()
