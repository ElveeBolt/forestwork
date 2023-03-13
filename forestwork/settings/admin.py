from django.contrib import admin
from .models import Country, Specialization, SpecializationCategory


# Register your models here.
@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ('title', 'a2', 'a3')


class SpecializationInline(admin.StackedInline):
    model = Specialization
    extra = 0


@admin.register(SpecializationCategory)
class SpecializationCategory(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (SpecializationInline,)


@admin.register(Specialization)
class Specialization(admin.ModelAdmin):
    list_display = ('title', 'category')