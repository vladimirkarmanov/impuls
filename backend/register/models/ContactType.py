from django.db import models

from core.validators import only_russian_chars


class ContactType(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[only_russian_chars])

    class Meta:
        verbose_name = 'Вид контакта'
        verbose_name_plural = 'Виды контактов'
        ordering = ['name']

    def __str__(self):
        return self.name
