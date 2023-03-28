from django.db import models
from jobs.models import Job
from django.conf import settings


class Chat(models.Model):
    TYPE_CHOICES = (
        (0, 'Предложение'),
        (1, 'Отклик на вакансию')
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок чата')
    job = models.ForeignKey(Job, null=True, verbose_name='Вакансия', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', null=False, verbose_name='Инициатор чата', on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    type = models.IntegerField(blank=True, default=0, choices=TYPE_CHOICES, verbose_name='Тип диалога')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'chats'
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['date_publish']


# Create your models here.
class Message(models.Model):
    chat = models.ForeignKey(Chat, null=True, verbose_name='Чат', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='sender_user', verbose_name='Отправитель', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Сообщение')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'messages'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['date_publish']