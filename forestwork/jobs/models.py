from django.db import models
from django.urls import reverse
from django.conf import settings
from settings.models import Country, Specialization


class Job(models.Model):
    STATAUS_CHOICES = (
        (0, 'Не активно'),
        (1, 'Активно')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    description = models.TextField(verbose_name='Описание')
    specialization = models.ForeignKey(Specialization, null=True, verbose_name='Специализация', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, verbose_name='Страна', on_delete=models.CASCADE)
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата ($)')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    status = models.IntegerField(blank=True, default=0, choices=STATAUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'
        ordering = ['-date_publish']
