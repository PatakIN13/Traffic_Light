from django.db import models


class Department(models.Model):

    parent_department = models.ForeignKey('Department', default=None, null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name="Родительское подразделение")
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        app_label = 'company'
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.name
