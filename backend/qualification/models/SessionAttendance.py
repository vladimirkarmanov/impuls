from django.db import models

from register.models.TeacherRole import TeacherRole


class SessionAttendance(models.Model):
    date = models.DateField(verbose_name='Дата')
    course = models.ForeignKey('Course',
                               on_delete=models.SET_NULL,
                               related_name='session_attendances',
                               blank=True,
                               null=True,
                               verbose_name='Дистанционный курс ПК')
    teacher_role = models.ForeignKey(TeacherRole,
                                     on_delete=models.SET_NULL,
                                     related_name='session_attendances',
                                     blank=True,
                                     null=True,
                                     verbose_name='Роль педагог')

    class Meta:
        verbose_name = 'Посещение сеанса обучения'
        verbose_name_plural = 'Посещения сеансов обучения'
        ordering = ['date']

    def __str__(self):
        return self.date
