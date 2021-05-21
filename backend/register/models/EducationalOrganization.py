from django.db import models

from core.validators import only_russian_chars


class EducationalOrganization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[only_russian_chars])
    short_name = models.CharField(max_length=50, verbose_name='Краткое название', validators=[only_russian_chars])

    class Meta:
        verbose_name = 'Образовательная организация'
        verbose_name_plural = 'Образовательные организации'
        ordering = ['name']

    def __str__(self):
        return self.name