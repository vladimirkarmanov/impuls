from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    patronymic = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    experience = models.PositiveSmallIntegerField(default=0)
    job_place = models.ForeignKey('JobPlace',
                                  on_delete=models.DO_NOTHING,
                                  related_name='users',
                                  null=True)
    job_position = models.ForeignKey('JobPosition',
                                     on_delete=models.DO_NOTHING,
                                     related_name='users',
                                     null=True)
    events = models.ManyToManyField('events.Event', related_name='users')

    def __str__(self):
        return f'Username: {self.username}, email: {self.email}'


class AdditionalUserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='additional_info')
    country = models.CharField(max_length=30, default='Россия')
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    mail_index = models.PositiveIntegerField(blank=True, null=True)
    about = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'Город: {self.city}, телефон: {self.phone}'


class JobPlace(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Наименование: {self.name}'


class JobPosition(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Наименование: {self.name}'
