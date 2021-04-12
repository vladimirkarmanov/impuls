from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .validators import only_russian_chars


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='Имя', validators=[only_russian_chars])
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', validators=[only_russian_chars])
    patronymic = models.CharField(max_length=30,
                                  blank=True,
                                  null=True,
                                  verbose_name='Отчество',
                                  validators=[only_russian_chars])
    experience = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name='Стаж')
    job_position = models.ForeignKey('JobPosition',
                                     on_delete=models.SET_NULL,
                                     related_name='users',
                                     blank=True,
                                     null=True,
                                     verbose_name='Должность')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'
        ordering = ['date_joined']

    def __str__(self):
        return f'Логин: {self.username}'

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name} '
        if self.patronymic:
            full_name += self.patronymic
        return full_name.strip()


class JobPosition(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[only_russian_chars])
    short_name = models.CharField(max_length=50, verbose_name='Краткое название', validators=[only_russian_chars])

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

    def __str__(self):
        return self.name


class EducationalOrganization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[only_russian_chars])
    short_name = models.CharField(max_length=50, verbose_name='Краткое название', validators=[only_russian_chars])

    class Meta:
        verbose_name = 'Образовательная организация'
        verbose_name_plural = 'Образовательные организации'
        ordering = ['name']

    def __str__(self):
        return self.name


class EducationalDocument(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    date = models.DateField(verbose_name='Дата выдачи')

    class Meta:
        verbose_name = 'Документ об образовании'
        verbose_name_plural = 'Документы об образовании'
        ordering = ['number']

    def __str__(self):
        return self.number
