from django.contrib import admin
from .models import FaqCategory, FaqQuestion


# Register your models here.
class HelpInline(admin.StackedInline):
    model = FaqQuestion
    extra = 0


@admin.register(FaqCategory)
class FaqCategory(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (HelpInline,)


@admin.register(FaqQuestion)
class Help(admin.ModelAdmin):
    list_display = ('title', 'category')
