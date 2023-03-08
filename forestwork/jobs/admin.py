from django.contrib import admin
from .models import Job


# Register your models here.
@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ('title', 'user', 'salary', 'date_publish')
    list_filter = ('salary', 'date_publish')
    readonly_fields = ('date_publish',)
