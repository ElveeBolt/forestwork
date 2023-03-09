from django.db import models


# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    a2 = models.CharField(max_length=2, unique=True, verbose_name='A2')
    a3 = models.CharField(primary_key=True, max_length=3, unique=True, verbose_name='A3')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'countries'
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'
        ordering = ['-title']
