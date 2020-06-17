from django.db import models
from django.utils.timezone import now


class Document(models.Model):
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    file = models.FileField(verbose_name='Файл')
    user = models.ForeignKey('register.User',
                             on_delete=models.CASCADE,
                             related_name='documents',
                             null=True,
                             verbose_name='Пользователь')
    document_type = models.ForeignKey('DocumentType',
                                      on_delete=models.DO_NOTHING,
                                      related_name='documents',
                                      verbose_name='Вид документа')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['number']

    def __str__(self):
        return self.number


class DocumentType(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    event = models.ForeignKey('events.Event',
                              on_delete=models.DO_NOTHING,
                              related_name='document_types',
                              verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Вид документа'
        verbose_name_plural = 'Виды документов'
        ordering = ['name']

    def __str__(self):
        return self.name


class Contract(models.Model):
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    status = models.BooleanField(default=True, verbose_name='Статус')
    start_date = models.DateField(default=now, verbose_name='Дата заключения')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата завершения')
    document_regulation = models.ForeignKey('DocumentRegulation',
                                            on_delete=models.DO_NOTHING,
                                            related_name='contracts',
                                            verbose_name='Документ регламент')
    user = models.ForeignKey('register.User',
                             on_delete=models.CASCADE,
                             related_name='contracts',
                             null=True,
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
        ordering = ['number']

    def __str__(self):
        return f'Номер: {self.number}, дата заключения: {self.start_date},' \
               f' статус: {"Активен" if self.status else "Неактивен"}'


class DocumentRegulation(models.Model):
    document_type = models.CharField(max_length=150, unique=True, verbose_name='Вид документа')

    class Meta:
        verbose_name = 'Регламент документа'
        verbose_name_plural = 'Регламенты документов'
        ordering = ['document_type']

    def __str__(self):
        return self.document_type
