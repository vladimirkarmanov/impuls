from django.db import models


class TrainingDocument(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер')
    date = models.DateField(verbose_name='Дата выдачи')
    number_of_hours = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Количество часов')

    class Meta:
        verbose_name = 'Документ о повышении квалификации'
        verbose_name_plural = 'Документы о повышении квалификации'
        ordering = ['date']

    def __str__(self):
        return str(self.number)
