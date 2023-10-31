from django.db import models


class Position(models.Model):

    name = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        app_label = 'company'
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name
