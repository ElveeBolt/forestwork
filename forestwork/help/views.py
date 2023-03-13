from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FaqCategory


# Create your views here.
class FaqListView(LoginRequiredMixin, ListView):
    model = FaqCategory
    template_name = 'help/faq.html'
    context_object_name = 'categories'
    extra_context = {
        'title': 'Помощь',
        'subtitle': 'Страница ответов на часто задаваемые вопросы'
    }
