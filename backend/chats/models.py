from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class MessageQueryset(models.QuerySet):
    def unreaded(self):
        return self.filter(is_readed=False)


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat'),
    )

    name = models.CharField(max_length=128, verbose_name='Название')
    type = models.CharField(max_length=1, choices=CHAT_TYPE_CHOICES, default=DIALOG, verbose_name='Тип')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Участник')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['name']

    def __str__(self):
        return f'{self.id} {self.type} {self.name}'

    def get_absolute_url(self):
        return reverse('chats:messages', kwargs={'chat_id': self.pk})


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.DO_NOTHING, verbose_name='Чат')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='messages',
                               on_delete=models.CASCADE,
                               verbose_name='Пользователь')
    text = models.TextField(verbose_name='Сообщение')
    created_dt = models.DateTimeField(default=timezone.now, verbose_name='Дата сообщения')
    is_readed = models.BooleanField(default=False, verbose_name='Прочитано')

    objects = MessageQueryset.as_manager()

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['created_dt']

    def __str__(self):
        return self.text
