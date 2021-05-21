from django.db import models

from register.models.TeacherRole import TeacherRole


class TrainingRequest(models.Model):
    date = models.DateField(verbose_name='Дата выдачи')
    course = models.ForeignKey('Course',
                               on_delete=models.SET_NULL,
                               related_name='training_requests',
                               blank=True,
                               null=True,
                               verbose_name='Дистанционный курс ПК')
    teacher_role = models.ForeignKey(TeacherRole,
                                     on_delete=models.SET_NULL,
                                     related_name='training_requests',
                                     blank=True,
                                     null=True,
                                     verbose_name='Роль педагог')

    class Meta:
        verbose_name = 'Заявка на повышение квалификации'
        verbose_name_plural = 'Заявки на повышение квалификации'
        ordering = ['date']

    def __str__(self):
        return self.date
