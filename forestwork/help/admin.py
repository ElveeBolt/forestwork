from django.contrib import admin
from .models import FaqCategory, FaqQuestion


# Register your models here.
class FaqQuestionInline(admin.StackedInline):
    model = FaqQuestion
    extra = 0


@admin.register(FaqCategory)
class FaqCategory(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (FaqQuestionInline,)


@admin.register(FaqQuestion)
class FaqQuestion(admin.ModelAdmin):
    list_display = ('title', 'category')
