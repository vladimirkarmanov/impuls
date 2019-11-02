from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150)
    organizer = models.ForeignKey('EventOrganizer',
                                  on_delete=models.DO_NOTHING,
                                  related_name='events')

    def __str__(self):
        return f'Наименование: {self.name}'


class EventOrganizer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=120)

    def __str__(self):
        return f'Наименование: {self.name}, телефон: {self.phone}'


class EventDate(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='dates')

    def __str__(self):
        return f'Дата начала: {self.start_date},' \
               f' дата окончания: {self.end_date}'


class PressRelease(models.Model):
    file = models.FileField()
    event_date = models.OneToOneField(EventDate,
                                      on_delete=models.CASCADE,
                                      primary_key=True,
                                      related_name='press_release')

    def __str__(self):
        return f'Пресс релиз: {self.file.name}'
