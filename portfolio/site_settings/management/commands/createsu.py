# images/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='spawnadmin',
                password=os.environ.get("CLOUDINARY_API_SECRET")
            )
        print('Superuser has been created.')