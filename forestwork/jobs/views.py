from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import JobForm
from .models import Job


# Create your views here.
def index(request):
    page = request.GET.get('page', 1)

    jobs = Job.objects.all().values().order_by('-date_publish')

    paginator = Paginator(jobs, settings.RESULTS_PER_PAGE)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1),
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'Список вакансий',
        'subtitle': 'Доступные вакансии от работодателей',
        'page_obj': page_obj
    }

    return render(request, 'jobs/index.html', context=context)


def job(request, job_id):
    # TODO: add functionality Job details page.

    context = {
        'title': 'Название вакансии',
        'subtitle': 'Детальная информация касательно вакансии'
    }
    job = Job.objects.get(id=job_id)
    context['job'] = job
    return render(request, 'jobs/job.html', context=context)


def job_add(request):
    context = {
        'title': 'Добавление вакансии',
        'subtitle': 'Страница добавления новой вакансии',
    }

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('/jobs')
    else:
        context['form'] = JobForm()

    return render(request, 'jobs/job_add.html', context=context)


def job_edit(request, job_id):
    # TODO: add functionality Job edit page.

    context = {
        'title': 'Редактирование вакансии',
        'subtitle': 'Страница редактирования вакансии'
    }
    return render(request, 'jobs/job_edit.html', context=context)