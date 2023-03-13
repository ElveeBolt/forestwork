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


class SpecializationCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'specializations_category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории специализаций'
        ordering = ['-title']


class Specialization(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название специализации')
    category = models.ForeignKey(SpecializationCategory, null=True, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'specializations'
        verbose_name = 'Специализацию'
        verbose_name_plural = 'Специализации'
        ordering = ['-title']