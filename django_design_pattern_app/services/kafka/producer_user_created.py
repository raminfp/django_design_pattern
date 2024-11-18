import json
from confluent_kafka import Producer
import socket

topic = 'topic_user_created'


class ProducerUserCreated:
    def __init__(self) -> None:
        """
        Initialize the ProducerUserCreated class.

        This method creates a Kafka producer and assigns it to the `producer` attribute.

        :return: None
        """
        conf = {'bootstrap.servers': "localhost:9092", 'client.id': socket.gethostname()}
        self.producer = Producer(conf)

    # This method will be called inside view for sending Kafka message
    def publish(self, method, body):
        """
        Publish a message to Kafka.

        This method takes a method and body as parameters and sends them to Kafka
        using the producer. The message will be sent to the topic defined in the
        `topic` variable with the key "key.user.created".

        :param method: The method to be sent. This is ignored and only included for
            compatibility with the method signature of the parent class.
        :param body: The body of the message to be sent.
        :return: None
        """
        print('Inside UserService: Sending to Kafka: ')
        print(body)
        self.producer.produce(topic, key="key.user.created", value=json.dumps(body))
