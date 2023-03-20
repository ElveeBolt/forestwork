from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, TemplateView, UpdateView, DetailView
from .forms import ProfileAboutForm, ProfileContactForm, ProfilePasswordForm
from jobs.models import Job, JobMessage
from django.contrib.auth import get_user_model


# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/index.html'
    extra_context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }


class ProfileJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'profile/jobs.html'
    extra_context = {
        'title': 'Мои вакансии',
        'subtitle': 'Опубликованные вами вакансии',
    }


class ProfileMainUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model
    form_class = ProfileAboutForm
    template_name = 'profile/main.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfileContactsUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model
    form_class = ProfileContactForm
    template_name = 'profile/contacts.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    form_class = ProfilePasswordForm
    template_name = 'profile/password.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }


class ProfileMessageListView(LoginRequiredMixin, ListView):
    model = JobMessage
    template_name = 'profile/messages.html'
    context_object_name = 'messages'
    extra_context = {
        'title': 'Мои сообщения',
        'subtitle': 'Список ваших сообщений',
    }


class ProfileMessageDetailView(LoginRequiredMixin, DetailView):
    model = JobMessage
    template_name = 'profile/message.html'
    context_object_name = 'message'
    extra_context = {
        'title': 'Сообщение',
        'subtitle': 'Детали сообщения',
    }
