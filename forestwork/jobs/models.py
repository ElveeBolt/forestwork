from django.db import models
from django.conf import settings


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    description = models.TextField(verbose_name='Описание')
    country = models.CharField(blank=True, max_length=255, verbose_name='Страна')
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата ($)')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
