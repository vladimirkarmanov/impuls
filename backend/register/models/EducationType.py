from django.db import models

from core.validators import only_russian_chars


class EducationType(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[only_russian_chars])

    class Meta:
        verbose_name = 'Вид образования'
        verbose_name_plural = 'Виды образований'
        ordering = ['name']

    def __str__(self):
        return self.name
