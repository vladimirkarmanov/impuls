from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import phone_regex, mail_index_regex


class User(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=30,
                                 verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30,
                                  blank=True,
                                  verbose_name='Отчество')
    email = models.EmailField(max_length=70,
                              verbose_name='Email')
    experience = models.PositiveSmallIntegerField(default=0,
                                                  blank=True,
                                                  verbose_name='Стаж')
    job_place = models.ForeignKey('JobPlace',
                                  on_delete=models.DO_NOTHING,
                                  related_name='users',
                                  blank=True,
                                  null=True,
                                  verbose_name='Место работы')
    job_position = models.ForeignKey('JobPosition',
                                     on_delete=models.DO_NOTHING,
                                     related_name='users',
                                     blank=True,
                                     null=True,
                                     verbose_name='Должность')

    def __str__(self):
        return f'Никнейм: {self.username}, email: {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class JobPlace(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работы'


class JobPosition(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='additional_info',
                                verbose_name='Пользователь')
    country = models.CharField(max_length=30,
                               default='Россия',
                               verbose_name='Страна')
    region = models.CharField(max_length=50,
                              verbose_name='Регион')
    city = models.CharField(max_length=30,
                            verbose_name='Город')
    address = models.CharField(max_length=120,
                               blank=True,
                               verbose_name='Адрес')
    phone = models.CharField(max_length=11,
                             blank=True,
                             null=True,
                             verbose_name='Телефон',
                             validators=[phone_regex])
    mail_index = models.PositiveIntegerField(blank=True,
                                             null=True,
                                             verbose_name='Почтовый индекс',
                                             validators=[mail_index_regex])
    about = models.TextField(max_length=500,
                             blank=True,
                             verbose_name='Обо мне')

    def __str__(self):
        return f'Город: {self.city}, телефон: {self.phone}'

    class Meta:
        verbose_name = 'Дополнительная информация о пользователе'
        verbose_name_plural = 'Дополнительная информация о пользователе'
