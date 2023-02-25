from django.conf import settings
from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job
from django.views.generic import ListView, DetailView


class JobListView(ListView):
    model = Job
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'jobs/index.html'
    context_object_name = 'job_list'
    ordering = ['-date_publish']
    extra_context = {
        'title': 'Список вакансий',
        'subtitle': 'Доступные вакансии от работодателей'
    }


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job.html'
    extra_context = {
        'title': 'Название вакансии',
        'subtitle': 'Детальная информация касательно вакансии',
    }


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
