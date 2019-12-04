from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from .validators import phone_regex, mail_index_regex, only_chars


class User(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя',
                                  validators=[only_chars])
    last_name = models.CharField(max_length=30,
                                 verbose_name='Фамилия',
                                 validators=[only_chars])
    patronymic = models.CharField(max_length=30,
                                  blank=True,
                                  verbose_name='Отчество',
                                  validators=[only_chars])
    email = models.EmailField(max_length=70,
                              verbose_name='Email')
    email_confirmed = models.BooleanField(default=False)
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

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()

    def activate_user_accout_after_email_confirm(self):
        self.is_active = True
        self.email_confirmed = True
        password = User.objects.make_random_password()
        self.set_password(password)
        self.email_user(subject='Доступ к аккаунту',
                        message=f'Ваш пароль: {password}')
        self.save()

    def add_user_to_group_listeners(self):
        group, created = Group.objects.get_or_create(name='Слушатели')
        group.user_set.add(self)
        group.save()

    def add_user_to_group_teachers(self):
        group, created = Group.objects.get_or_create(name='Преподаватели')
        group.user_set.add(self)
        group.save()

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

    def __str__(self):
        return f'Город: {self.city}, телефон: {self.phone}'

    class Meta:
        verbose_name = 'Дополнительная информация о пользователе'
        verbose_name_plural = 'Дополнительная информация о пользователе'
