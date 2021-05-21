from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=50, verbose_name='Краткое название')

    class Meta:
        verbose_name = 'Дистанционный курс ПК'
        verbose_name_plural = 'Дистанционные курсы ПК'
        ordering = ['name']

    def __str__(self):
        return self.name
