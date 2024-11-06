from django.core.management.base import BaseCommand
from django_design_pattern_app.models import Representations
import os

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
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
