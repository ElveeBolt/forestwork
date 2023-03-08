from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'name', 'email', 'type', 'is_staff', 'is_active']
    list_filter = ['type', 'is_staff', 'is_active']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Основные данные',
            {
                'fields': ['name', 'type', 'about', 'country', 'city']
            }
        ),
        (
            'Контакты',
            {
                'fields': ['email', 'phone', 'telegram', 'whatsapp', 'linkedin', 'github', 'website', 'portfolio']
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Основные данные',
            {
                'fields': ['name', 'type', 'about', 'country', 'city']
            }
        ),
        (
            'Контакты',
            {
                'fields': ['phone', 'telegram', 'whatsapp', 'linkedin', 'github', 'website', 'portfolio']
            }
        )
    )
