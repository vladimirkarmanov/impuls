from django.db import models

from register.models.TeacherRole import TeacherRole


class TrainingDocument(models.Model):
    date = models.DateField(verbose_name='Дата выдачи')
    number_of_hours = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Количество часов')
    course = models.ForeignKey('Course',
                               on_delete=models.SET_NULL,
                               related_name='training_docs',
                               blank=True,
                               null=True,
                               verbose_name='Дистанционный курс ПК')
    teacher_role = models.ForeignKey(TeacherRole,
                                     on_delete=models.SET_NULL,
                                     related_name='training_docs',
                                     blank=True,
                                     null=True,
                                     verbose_name='Роль педагог')

    class Meta:
        verbose_name = 'Документ о повышении квалификации'
        verbose_name_plural = 'Документы о повышении квалификации'
        ordering = ['date']

    def __str__(self):
        return self.date
