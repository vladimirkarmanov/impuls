from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    patronymic = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    experience = models.PositiveSmallIntegerField(default=0)
    job_place = models.ForeignKey('JobPlace', on_delete=models.DO_NOTHING,
                                  related_name='users',
                                  null=True)

    def __str__(self):
        return f'Username: {self.username}, email: {self.email}'


class JobPlace(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Наименование: {self.name}'
