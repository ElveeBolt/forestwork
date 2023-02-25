from django.conf import settings
from .forms import JobForm
from .models import Job
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
    context_object_name = 'job'
    extra_context = {
        'title': 'Название вакансии',
        'subtitle': 'Детальная информация касательно вакансии',
    }


class JobAddView(CreateView):
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    extra_context = {
        'title': 'Добавление вакансии',
        'subtitle': 'Страница добавления новой вакансии',
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    extra_context = {
        'title': 'Редактирование вакансии',
        'subtitle': 'Страница редактирования вакансии',
    }


class JobDeleteView(DeleteView):
    model = Job
    success_url = "/users/profile/jobs"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user
        )
