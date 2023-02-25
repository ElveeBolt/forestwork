from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import auth
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import LoginForm, RegisterForm, UserContactForm, UserAboutForm, UserPasswordForm
from jobs.models import Job
from .models import User
from django.views.generic import ListView, DetailView, TemplateView, UpdateView


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


class ProfileView(TemplateView):
    template_name = 'profile/index.html'
    extra_context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }


class ProfileJobListView(ListView):
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


class ProfileMainUpdateView(UpdateView):
    model = User
    form_class = UserAboutForm
    template_name = 'profile/main.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


def profile_contacts(request):
    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
        'form': UserContactForm(instance=request.user)
    }

    if request.method == 'POST':
        form = UserContactForm(request.POST, instance=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/users/profile')

    return render(request, 'profile/contacts.html', context=context)


def profile_password(request):
    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
        'form': UserPasswordForm(request.user)
    }

    if request.method == 'POST':
        form = UserPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/users/profile')

        context['form'] = form

    return render(request, 'profile/password.html', context=context)


def login(request):
    context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
        'form': LoginForm()
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Пользователь с таким именем и паролем не найден')

        context['form'] = form

    return render(request, 'users/login.html', context=context)


def register(request):
    context = {
        'title': 'Регистрация профиля',
        'subtitle': 'Создайте профиль для того, чтобы использовать преимущества ForestWork',
        'form': RegisterForm()
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            auth.login(request, user)
            return redirect('/')
        else:
            context['form'] = form

    return render(request, 'users/register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')
