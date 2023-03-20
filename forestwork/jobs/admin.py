from django.contrib import admin
from .models import Job, JobMessage


# Register your models here.
@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ('title', 'user', 'salary', 'date_publish', 'status')
    list_filter = ('salary', 'date_publish', 'status')
    readonly_fields = ('date_publish',)


@admin.register(JobMessage)
class JobMessage(admin.ModelAdmin):
    list_display = ('title', 'user', 'job', 'date_publish')
    readonly_fields = ('date_publish',)
