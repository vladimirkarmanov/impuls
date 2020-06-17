from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    organizer = models.ForeignKey('EventOrganizer',
                                  on_delete=models.DO_NOTHING,
                                  related_name='events',
                                  verbose_name='Организатор')
    users = models.ManyToManyField('register.User',
                                   related_name='events',
                                   blank=True,
                                   verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name']

    def __str__(self):
        return self.name


class EventOrganizer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=120, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'
        ordering = ['name']

    def __str__(self):
        return f'Наименование: {self.name}, телефон: {self.phone}'


class EventDate(models.Model):
    start_date = models.DateTimeField(null=True, verbose_name='Дата начала')
    end_date = models.DateTimeField(null=True, verbose_name='Дата окончания')
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='dates',
                              verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Дата мероприятия'
        verbose_name_plural = 'Даты мероприятий'
        ordering = ['start_date']

    def __str__(self):
        return f'Дата начала: {self.start_date}, дата окончания: {self.end_date}'


class PressRelease(models.Model):
    file = models.FileField(verbose_name='Файл')
    event_date = models.OneToOneField(EventDate,
                                      on_delete=models.DO_NOTHING,
                                      primary_key=True,
                                      related_name='press_release',
                                      verbose_name='Дата мероприятия')

    class Meta:
        verbose_name = 'Пресс релиз'
        verbose_name_plural = 'Пресс релизы'

    def __str__(self):
        return self.file.name
