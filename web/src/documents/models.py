from django.db import models


class Document(models.Model):
    number = models.CharField(max_length=50)
    file = models.FileField()
    user = models.ForeignKey('register.User',
                             on_delete=models.CASCADE,
                             related_name='documents',
                             null=True)
    document_type = models.ForeignKey('DocumentType',
                                      on_delete=models.CASCADE,
                                      related_name='documents')

    def __str__(self):
        return f'Номер: {self.number}'


class DocumentType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    event = models.ForeignKey('events.Event',
                              on_delete=models.DO_NOTHING,
                              related_name='document_types')

    def __str__(self):
        return f'Наименование: {self.name}'


class Contract(models.Model):
    number = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField(default=False)
    document_regulation = models.ForeignKey('DocumentRegulation',
                                            on_delete=models.DO_NOTHING,
                                            related_name='contracts')
    user = models.ForeignKey('register.User',
                             on_delete=models.CASCADE,
                             related_name='contracts',
                             null=True)

    def __str__(self):
        return f'Номер: {self.number}, дата: {self.date},' \
               f' статус: {self.status}'


class DocumentRegulation(models.Model):
    document_type = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'Вид документа: {self.document_type}'
