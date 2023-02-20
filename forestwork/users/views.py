from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import auth
from .forms import LoginForm, RegisterForm


# Create your views here.
def index(request):
    # TODO: add functionality users list page.

    context = {
        'title': 'Список пользователей',
        'subtitle': 'Все пользователи сайта'
    }
    return render(request, 'users/index.html', context=context)


def employers(request):
    # TODO: add functionality employers list page.

    context = {
        'title': 'Работодатели',
        'subtitle': 'Список работодателей и компаний'
    }
    return render(request, 'users/employers.html', context=context)


def employer(request, user_id):
    # TODO: add functionality employer details page.

    context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о работодателе или компании'
    }
    return render(request, 'users/employer.html', context=context)


def developers(request):
    # TODO: add functionality developers list page.

    context = {
        'title': 'Разработчики',
        'subtitle': 'Список разработчиков'
    }
    return render(request, 'users/developers.html', context=context)


def developer(request, user_id):
    # TODO: add functionality developer details page.

    context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о разработчике'
    }
    return render(request, 'users/developer.html', context=context)


def profile(request):
    # TODO: add functionality profile page.

    context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }
    return render(request, 'profile/index.html', context=context)


def profile_edit(request):
    # TODO: add functionality edit profile page.

    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля'
    }
    return render(request, 'profile/edit.html', context=context)


def login(request):
    context = {
        'title': 'Авторизация',
        'subtitle': 'Страница авторизации пользователя',
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
