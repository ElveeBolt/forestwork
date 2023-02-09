from django.shortcuts import render


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
