from django.core.management.base import BaseCommand
from django_design_pattern_app.services.kafka.queue_listener import UserCreatedListener


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : Kafka'

    def handle(self, *args, **options):
        """
        Starts a new thread that runs the Kafka Consumer and starts consuming messages
        from the user_created topic.

        :param args: Not used
        :param options: Not used
        :return: None
        """
        td = UserCreatedListener()
        td.start()
        self.stdout.write("Started Consumer Thread")
