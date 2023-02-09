from django.shortcuts import render


# Create your views here.
def index(request):
    # TODO: add functionality Job list page.

    context = {
        'title': 'Список вакансий',
        'subtitle': 'Доступные вакансии от работодателей'
    }
    return render(request, 'jobs/index.html', context=context)


def job(request, job_id):
    # TODO: add functionality Job details page.

    context = {
        'title': 'Название вакансии',
        'subtitle': 'Детальная информация касательно вакансии'
    }
    return render(request, 'jobs/job.html', context=context)


def job_add(request):
    # TODO: add functionality Job add page.

    context = {
        'title': 'Добавление вакансии',
        'subtitle': 'Страница добавления новой вакансии'
    }
    return render(request, 'jobs/job_add.html', context=context)


def job_edit(request, job_id):
    # TODO: add functionality Job edit page.

    context = {
        'title': 'Редактирование вакансии',
        'subtitle': 'Страница редактирования вакансии'
    }
    return render(request, 'jobs/job_edit.html', context=context)
