from django.db import models
from django.urls import reverse
from django.conf import settings
from settings.models import Country, Specialization


class Job(models.Model):
    STATUS_CHOICES = (
        (0, 'Не активно'),
        (1, 'Активно')
    )

    REMOTE_TYPE_CHOICES = (
        (0, 'Не выбрано'),
        (1, 'На выбор кандидата'),
        (2, 'Только офис'),
        (3, 'Гибридная работа'),
        (4, 'Только удалённо')
    )

    EXP_CHOICES = (
        (0, 'Не выбрано'),
        (1, 'Без опыта работы'),
        (2, '1 год'),
        (3, '2 года'),
        (4, '3 года'),
        (5, '5 лет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    description = models.TextField(verbose_name='Описание')
    specialization = models.ForeignKey(Specialization, null=True, verbose_name='Специализация', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, verbose_name='Страна', on_delete=models.CASCADE)
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата ($)')
    remote_type = models.IntegerField(blank=True, default=0, choices=REMOTE_TYPE_CHOICES, verbose_name='Удалённая работа / Офис')
    exp = models.IntegerField(blank=True, default=0, choices=EXP_CHOICES, verbose_name='Опыт работы')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    date_publish = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    status = models.IntegerField(blank=True, default=0, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'
        ordering = ['-date_publish']
