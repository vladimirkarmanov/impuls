from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .validators import only_chars


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='Имя', validators=[only_chars])
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', validators=[only_chars])
    patronymic = models.CharField(max_length=30,
                                  blank=True,
                                  null=True,
                                  verbose_name='Отчество',
                                  validators=[only_chars])
    email = models.EmailField(max_length=70, unique=True, verbose_name='Email')
    email_confirmed = models.BooleanField(default=False)
    experience = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name='Стаж')
    job_position = models.ForeignKey('JobPosition',
                                     on_delete=models.SET_NULL,
                                     related_name='users',
                                     blank=True,
                                     null=True,
                                     verbose_name='Должность')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['date_joined']

    def __str__(self):
        return f'Никнейм: {self.username}, email: {self.email}'

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name} '
        if self.patronymic:
            full_name += self.patronymic
        return full_name.strip()


class JobPosition(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

    def __str__(self):
        return self.name


class EducationalOrganization(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=50, verbose_name='Краткое название')

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
