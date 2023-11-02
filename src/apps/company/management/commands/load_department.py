from django.core.management.base import BaseCommand

from apps.company.models import Department


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.department = ['Администрация', 'Инженерный отдел', 'Офис', 'Бухгалтерия', 'IT отдел']

    def load_department_child(self, department, count):
        if count > 5:
            return 0
        for data in self.department:
            department_child = Department()
            department_child.name = data
            department_child.parent_department = department
            department_child.save()
            count += 1
            self.load_department_child(department_child, count)

    def load_department(self):
        for data in self.department:
            department = Department()
            department.name = data
            department.save()
            self.load_department_child(department, 1)

    def handle(self, *args, **options):
        self.load_department()

        print('finished department')
