from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.models import auth
from .forms import LoginForm, RegisterForm, UserContactForm, UserAboutForm, UserPasswordForm


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


def profile_main(request):
    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
        'form': UserAboutForm(initial={
            'name': request.user.name,
            'about': request.user.about
        })
    }

    if request.method == 'POST':
        form = UserAboutForm(request.POST)
        user = request.user
        if form.is_valid():
            about = form.save(commit=False)
            user.about = about.about
            user.name = about.name
            user.save()
            return redirect('/users/profile')

    return render(request, 'profile/main.html', context=context)


def profile_contacts(request):
    context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
        'form': UserContactForm(initial={
            'country': request.user.country,
            'city': request.user.city,
            'phone': request.user.phone,
            'telegram': request.user.telegram,
            'whatsapp': request.user.whatsapp,
            'linkedin': request.user.linkedin,
            'github': request.user.github,
            'website': request.user.website,
            'portfolio': request.user.portfolio,
        })
    }

    if request.method == 'POST':
        form = UserContactForm(request.POST)
        user = request.user
        if form.is_valid():
            contacts = form.save(commit=False)
            user.country = contacts.country
            user.city = contacts.city
            user.phone = contacts.phone
            user.telegram = contacts.telegram
            user.whatsapp = contacts.whatsapp
            user.linkedin = contacts.linkedin
            user.github = contacts.github
            user.website = contacts.website
            user.portfolio = contacts.portfolio
            user.save()
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
