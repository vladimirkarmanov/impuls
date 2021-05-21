from django.db import models


class EducationalDocument(models.Model):
    date = models.DateField(verbose_name='Дата выдачи')
    education_type = models.ForeignKey('EducationType',
                                       on_delete=models.SET_NULL,
                                       related_name='educational_docs',
                                       blank=True,
                                       null=True,
                                       verbose_name='Вид образования')
    teacher_role = models.ForeignKey('TeacherRole',
                                     on_delete=models.SET_NULL,
                                     related_name='educational_docs',
                                     blank=True,
                                     null=True,
                                     verbose_name='Роль педагог')

    class Meta:
        verbose_name = 'Документ об образовании'
        verbose_name_plural = 'Документы об образовании'
        ordering = ['date']

    def __str__(self):
        return self.date
