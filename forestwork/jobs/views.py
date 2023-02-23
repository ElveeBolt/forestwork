from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import JobForm
from .models import Job
from django.forms.models import model_to_dict



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
            return redirect('/users/profile/jobs')
    else:
        context['form'] = JobForm()

    return render(request, 'jobs/job_form.html', context=context)


def job_edit(request, job_id):
    context = {
        'title': 'Редактирование вакансии',
        'subtitle': 'Страница редактирования вакансии',
    }

    instance = Job.objects.get(id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/users/profile/jobs')
    else:
        context['form'] = JobForm(instance=instance)

    return render(request, 'jobs/job_form.html', context=context)


def job_delete(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        if job.user == request.user:
            Job.objects.filter(id=job_id).delete()
            return redirect('/users/profile/jobs')