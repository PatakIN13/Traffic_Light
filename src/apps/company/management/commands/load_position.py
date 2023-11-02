from django.core.management.base import BaseCommand

from apps.company.models import Position


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.position = ['Директор', 'Менеджер', 'Бухгалтер', 'Инженер', 'Техник']

    def load_position(self):
        for data in self.position:
            position = Position()
            position.name = data
            position.save()

    def handle(self, *args, **options):
        self.load_position()

        print('finished position')
