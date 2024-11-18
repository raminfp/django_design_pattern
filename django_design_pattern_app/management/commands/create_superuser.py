from django.core.management.base import BaseCommand
from django_design_pattern_app.models import Users
import os

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
        """
        Handles the creation of a superuser.

        Checks if a superuser with the given username (from the SUPERUSER_USERNAME
        environment variable) already exists. If it does, outputs a warning message.
        Otherwise, creates a new superuser with the given email (from the
        SUPERUSER_EMAIL environment variable) and password (from the
        SUPERUSER_PASSWORD environment variable), and outputs a success message.
        """
        if Users.objects.filter(username=os.getenv("SUPERUSER_USERNAME")).exists():
            self.stdout.write(self.style.WARNING("Superuser already exists."))
        else:
            Users.objects.create_superuser(
                username=os.getenv("SUPERUSER_USERNAME"),
                email=os.getenv("SUPERUSER_EMAIL"),
                password=os.getenv("SUPERUSER_PASSWORD"),
                is_superuser=True,
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
