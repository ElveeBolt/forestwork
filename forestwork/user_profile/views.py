from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, TemplateView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import ProfileAboutForm, ProfileContactForm, ProfilePasswordForm
from jobs.models import Job
from chat.models import Chat, Message
from chat.forms import AnswerMessageForm
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
    model = Chat
    template_name = 'profile/messages.html'
    context_object_name = 'chats'
    extra_context = {
        'title': 'Мои сообщения',
        'subtitle': 'Список ваших сообщений',
    }

    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user)


class ProfileMessageDetailView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = 'profile/message.html'
    form_class = AnswerMessageForm
    extra_context = {
        'title': 'Сообщение',
        'subtitle': 'Детали сообщения',
    }

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = Chat.objects.get(id=self.kwargs['pk'])
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.chat = self.object
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(chat=self.kwargs['pk'])
        context['chat'] = Chat.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('profile_message', kwargs={'pk': self.object.pk})
