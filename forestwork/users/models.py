from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from settings.models import Country, Specialization


# Create your models here.
class User(AbstractUser):
    PROFILE_CHOICES = [
        (0, 'Кандидат'),
        (1, 'Работодатель')
    ]

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

    name = models.CharField(max_length=255, verbose_name='Имя')
    type = models.IntegerField(choices=PROFILE_CHOICES, default=0, verbose_name='Тип профиля')
    about = models.TextField(blank=True, verbose_name='Дополнительная информация')
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.CASCADE, null=True)
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    phone = models.CharField(blank=True, max_length=255, verbose_name='Телефон')
    telegram = models.CharField(blank=True, max_length=255, verbose_name='Telegram')
    whatsapp = models.CharField(blank=True, max_length=255, verbose_name='WhatsApp')
    linkedin = models.CharField(blank=True, max_length=255, verbose_name='LinkedIn')
    github = models.CharField(blank=True, max_length=255, verbose_name='GitHub')
    website = models.CharField(blank=True, max_length=255, verbose_name='Веб-сайт')
    portfolio = models.CharField(blank=True, max_length=255, verbose_name='Портфолио')
    specialization = models.ForeignKey(Specialization, null=True, verbose_name='Специализация', on_delete=models.CASCADE)
    remote_type = models.IntegerField(blank=True, default=0, choices=REMOTE_TYPE_CHOICES, verbose_name='Удалённая работа / Офис')
    exp = models.IntegerField(blank=True, default=0, choices=EXP_CHOICES, verbose_name='Опыт работы')
    is_active = models.BooleanField(default=False, verbose_name='Активный')

    def get_absolute_url(self):
        return reverse('profile')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
