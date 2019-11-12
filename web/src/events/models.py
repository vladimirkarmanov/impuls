from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Наименование')
    organizer = models.ForeignKey('EventOrganizer',
                                  on_delete=models.DO_NOTHING,
                                  related_name='events',
                                  verbose_name='Организатор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class EventOrganizer(models.Model):
    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name='Наименование')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=120, verbose_name='Адрес')

    def __str__(self):
        return f'Наименование: {self.name}, телефон: {self.phone}'

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'


class EventDate(models.Model):
    start_date = models.DateField(null=True,
                                  verbose_name='Дата начала')
    end_date = models.DateField(null=True,
                                verbose_name='Дата окончания')
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='dates',
                              verbose_name='Мероприятие')

    def __str__(self):
        return f'Дата начала: {self.start_date},' \
               f' дата окончания: {self.end_date}'

    class Meta:
        verbose_name = 'Дата мероприятия'
        verbose_name_plural = 'Даты мероприятий'


class PressRelease(models.Model):
    file = models.FileField(verbose_name='Файл')
    event_date = models.OneToOneField(EventDate,
                                      on_delete=models.DO_NOTHING,
                                      primary_key=True,
                                      related_name='press_release',
                                      verbose_name='Дата мероприятия')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Пресс релиз'
        verbose_name_plural = 'Пресс релизы'
