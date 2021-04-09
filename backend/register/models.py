from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .validators import phone_regex, mail_index_regex, only_chars


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
    job_place = models.ForeignKey('JobPlace',
                                  on_delete=models.SET_NULL,
                                  related_name='users',
                                  blank=True,
                                  null=True,
                                  verbose_name='Место работы')
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


class JobPlace(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работы'
        ordering = ['name']

    def __str__(self):
        return self.name


class JobPosition(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

    def __str__(self):
        return self.name


class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='additional_info',
                                verbose_name='Пользователь')
    country = models.CharField(max_length=30,
                               default='Россия',
                               verbose_name='Страна',
                               validators=[only_chars])
    region = models.CharField(max_length=50,
                              verbose_name='Регион',
                              validators=[only_chars])
    city = models.CharField(max_length=30,
                            verbose_name='Город',
                            validators=[only_chars])
    address = models.CharField(max_length=120,
                               verbose_name='Адрес')
    phone = models.CharField(max_length=11,
                             verbose_name='Телефон',
                             validators=[phone_regex])
    mail_index = models.CharField(max_length=6,
                                  verbose_name='Почтовый индекс',
                                  validators=[mail_index_regex])
    about = models.TextField(max_length=500,
                             verbose_name='Обо мне')

    class Meta:
        verbose_name = 'Дополнительная информация о пользователе'
        verbose_name_plural = 'Дополнительная информация о пользователе'

    def __str__(self):
        return f'Город: {self.city}, телефон: {self.phone}'


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
