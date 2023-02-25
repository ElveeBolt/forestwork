from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import auth
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def employers(request):
    page = request.GET.get('page', 1)

    users = User.objects.filter(type=1).all().values()

    paginator = Paginator(users, settings.RESULTS_PER_PAGE)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1),
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Работодатели',
        'subtitle': 'Список работодателей и компаний',
        'page_obj': page_obj
    }
    return render(request, 'users/employers.html', context=context)


def employer(request, user_id):
    context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о работодателе или компании',
        'user_info': User.objects.get(id=user_id)
    }
    return render(request, 'users/user.html', context=context)


def developers(request):
    page = request.GET.get('page', 1)

    users = User.objects.filter(type=0).all().values()

    paginator = Paginator(users, settings.RESULTS_PER_PAGE)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1),
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Разработчики',
        'subtitle': 'Список разработчиков',
        'page_obj': page_obj
    }
    return render(request, 'users/developers.html', context=context)


def developer(request, user_id):
    context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о разработчике',
        'user_info': User.objects.get(id=user_id)
    }
    return render(request, 'users/user.html', context=context)


def profile(request):
    context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }
    return render(request, 'profile/index.html', context=context)


def profile_jobs(request):
    context = {
        'title': 'Мои вакансии',
        'subtitle': 'Опубликованные вами вакансии',
        'jobs': Job.objects.filter(user=request.user).all().values()
    }

    return render(request, 'profile/jobs.html', context=context)


def profile_main(request):
    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
        'form': UserAboutForm(instance=request.user)
    }

    if request.method == 'POST':
        form = UserAboutForm(request.POST, instance=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('/users/profile')

    return render(request, 'profile/main.html', context=context)


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
        'subtitle': 'Страница регистрации пользователя',
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
