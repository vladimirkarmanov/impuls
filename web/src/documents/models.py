from django.db import models


class Document(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер')
    file = models.FileField(verbose_name='Файл')
    user = models.ForeignKey('register.User',
                             on_delete=models.CASCADE,
                             related_name='documents',
                             null=True, verbose_name='Пользователь')
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE,
                                      related_name='documents',
                                      verbose_name='Вид документа')

    def __str__(self):
        return f'Номер: {self.number}'


class DocumentType(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование')
    event = models.ForeignKey('events.Event', on_delete=models.DO_NOTHING,
                              related_name='document_types',
                              verbose_name='Мероприятие')

    def __str__(self):
        return f'Наименование: {self.name}'


class Contract(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер')
    date = models.DateField(verbose_name='Дата')
    status = models.BooleanField(default=False, verbose_name='Статус')
    document_regulation = models.ForeignKey('DocumentRegulation',
                                            on_delete=models.DO_NOTHING,
                                            related_name='contracts',
                                            verbose_name='Документ регламент')
    user = models.ForeignKey('register.User', on_delete=models.CASCADE,
                             related_name='contracts', null=True,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'Номер: {self.number}, дата: {self.date},' \
               f' статус: {self.status}'


class DocumentRegulation(models.Model):
    document_type = models.CharField(max_length=150, unique=True,
                                     verbose_name='Вид документа')

    def __str__(self):
        return f'Вид документа: {self.document_type}'
