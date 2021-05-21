from django.db import models

from core.validators import only_russian_chars


class PhysicalFace(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя', validators=[only_russian_chars])
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', validators=[only_russian_chars])
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', validators=[only_russian_chars])
    experience = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name='Стаж')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'
        ordering = ['first_name']

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        return full_name.strip()
