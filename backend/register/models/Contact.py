from django.db import models

from core.validators import phone_regex


class Contact(models.Model):
    contact_number = models.CharField(max_length=150, unique=True, verbose_name='Название', validators=[phone_regex])
    contact_type = models.ForeignKey('ContactType',
                                     on_delete=models.SET_NULL,
                                     related_name='contact_numbers',
                                     blank=True,
                                     null=True,
                                     verbose_name='Вид контакта')
    teacher_role = models.ForeignKey('TeacherRole',
                                     on_delete=models.SET_NULL,
                                     related_name='contact_numbers',
                                     blank=True,
                                     null=True,
                                     verbose_name='Роль педагог')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['contact_type']

    def __str__(self):
        return self.contact_number
