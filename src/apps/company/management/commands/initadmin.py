from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = 'admin'
        password = 'P@ssw0rd'
        email = ''

        User.objects.create_superuser(username=username, email=email, password=password)
