from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    organizer = models.ForeignKey('EventOrganizer',
                                  on_delete=models.DO_NOTHING,
                                  related_name='events',
                                  verbose_name='Организатор')

    def __str__(self):
        return f'Наименование: {self.name}'


class EventOrganizer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=120, verbose_name='Адрес')

    def __str__(self):
        return f'Наименование: {self.name}, телефон: {self.phone}'


class EventDate(models.Model):
    start_date = models.DateField(blank=True, null=True,
                                  verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True,
                                verbose_name='Дата окончания')
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='dates',
                              verbose_name='Мероприятие')

    def __str__(self):
        return f'Дата начала: {self.start_date},' \
               f' дата окончания: {self.end_date}'


class PressRelease(models.Model):
    file = models.FileField(verbose_name='Файл')
    event_date = models.OneToOneField(EventDate, on_delete=models.CASCADE,
                                      primary_key=True,
                                      related_name='press_release',
                                      verbose_name='Дата мероприятия')

    def __str__(self):
        return f'Пресс релиз: {self.file.name}'
