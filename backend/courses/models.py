from django.db import models


class Course(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=50, verbose_name='Краткое название')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']

    def __str__(self):
        return self.name
