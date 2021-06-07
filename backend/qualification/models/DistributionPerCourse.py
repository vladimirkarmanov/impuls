from django.db import models


class DistributionPerCourse(models.Model):
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    course = models.ForeignKey('Course',
                               on_delete=models.SET_NULL,
                               related_name='distributions_per_course',
                               blank=True,
                               null=True,
                               verbose_name='Дистанционный курс ПК')

    class Meta:
        verbose_name = 'Распределение на курс'
        verbose_name_plural = 'Распределения на курсы'
        ordering = ['date_start']

    def __str__(self):
        return self.date_start.strftime('%d.%m.%Y')
