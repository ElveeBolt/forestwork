from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    PROFILE_CHOICES = [
        (0, 'Кандидат'),
        (1, 'Работодатель')
    ]

    name = models.CharField(max_length=255, verbose_name='Имя')
    type = models.IntegerField(choices=PROFILE_CHOICES, default=0, verbose_name='Тип профиля')
    about = models.TextField(blank=True, verbose_name='Дополнительная информация')
    country = models.CharField(blank=True, max_length=255, verbose_name='Страна')
    city = models.CharField(blank=True, max_length=255, verbose_name='Город')
    phone = models.CharField(blank=True, max_length=255, verbose_name='Телефон')
    telegram = models.CharField(blank=True, max_length=255, verbose_name='Telegram')
    whatsapp = models.CharField(blank=True, max_length=255, verbose_name='WhatsApp')
    linkedin = models.CharField(blank=True, max_length=255, verbose_name='LinkedIn')
    github = models.CharField(blank=True, max_length=255, verbose_name='GitHub')
    website = models.CharField(blank=True, max_length=255, verbose_name='Веб-сайт')
    portfolio = models.CharField(blank=True, max_length=255, verbose_name='Портфолио')

    class Meta:
        ordering = ['-date_joined']
