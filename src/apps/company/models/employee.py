from datetime import datetime
from django.db import models
from .position import Position
from .department import Department


class Employee(models.Model):

    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=20, verbose_name="Отчество", null=True, blank=True)
    position = models.ForeignKey(Position, verbose_name="Должность", on_delete=models.CASCADE)
    recruitment = models.DateField(verbose_name="Прием на работу", default=datetime.now)
    salary_size = models.CharField(max_length=20, verbose_name="Размер заработной платы")
    department = models.ForeignKey(Department, verbose_name="Подразделение", on_delete=models.CASCADE)

    class Meta:
        app_label = 'company'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} {self.department} {self.position}'
