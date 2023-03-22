from django.contrib import admin
from .models import Message, Chat


# Register your models here.
@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ('user', 'date_publish')
    readonly_fields = ('date_publish',)


# Register your models here.
@admin.register(Chat)
class Chat(admin.ModelAdmin):
    readonly_fields = ('date_publish',)
