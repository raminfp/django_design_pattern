from django.core.management.base import BaseCommand
from django_design_pattern_app.models import Representations
import os


class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
        if Representations.objects.filter(username=os.getenv("SUPERUSER_USERNAME")).exists():
            pass
        else:
            Representations.objects.create_superuser(
                username=os.getenv("SUPERUSER_USERNAME"),
                email=os.getenv("SUPERUSER_EMAIL"),
                password=os.getenv("SUPERUSER_PASSWORD"),
                agency_code=0,
                is_superuser=True,
                is_active=True
            )
