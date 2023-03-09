from django.contrib import admin
from .models import Country


# Register your models here.
@admin.register(Country)
class Job(admin.ModelAdmin):
    list_display = ('title', 'a2', 'a3')
