from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView
from .forms import LoginForm, RegisterForm, UserContactForm, UserAboutForm, UserPasswordForm
from jobs.models import Job
from .models import User


# Create your views here.
def index(request):
    # TODO: add functionality users list page.

    context = {
        'title': 'Список пользователей',
        'subtitle': 'Все пользователи сайта'
    }
    return render(request, 'users/index.html', context=context)


class EmployerListView(ListView):
    model = User
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'users/employers.html'
    context_object_name = 'employers'
    ordering = ['-date_joined']
    extra_context = {
        'title': 'Работодатели',
        'subtitle': 'Список работодателей и компаний',
    }

    def get_queryset(self):
        return User.objects.filter(type=1)


class EmployerDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user_info'
    extra_context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о работодателе или компании',
    }


class DeveloperListView(ListView):
    model = User
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'users/developers.html'
    context_object_name = 'developers'
    ordering = ['-date_joined']
    extra_context = {
        'title': 'Разработчики',
        'subtitle': 'Список разработчиков',
    }

    def get_queryset(self):
        return User.objects.filter(type=0)


class DeveloperDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user_info'
    extra_context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о разработчике',
    }


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/index.html'
    extra_context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }


class ProfileJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'profile/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-date_joined']
    extra_context = {
        'title': 'Мои вакансии',
        'subtitle': 'Опубликованные вами вакансии',
    }

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


class ProfileMainUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserAboutForm
    template_name = 'profile/main.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfileContactsUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserContactForm
    template_name = 'profile/contacts.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordForm
    template_name = 'profile/password.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
    }


class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация профиля',
        'subtitle': 'Создайте профиль для того, чтобы использовать преимущества ForestWork',
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
