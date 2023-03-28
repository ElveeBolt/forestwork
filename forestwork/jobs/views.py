from django.conf import settings
from .forms import JobForm
from chat.models import Chat
from chat.forms import JobMessageForm
from .models import Job
from .utils import UserCheckTypeEmployerMixin, UserCheckJobAuthorMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin


class JobListView(ListView):
    model = Job
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'jobs/index.html'
    context_object_name = 'job_list'
    extra_context = {
        'title': 'Список вакансий',
        'subtitle': 'Доступные вакансии от работодателей'
    }

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET.get('query')

        if query:
            return queryset.filter(title__icontains=query, status=1)

        return queryset.filter(status=1)


class JobDetailView(FormMixin, DetailView):
    model = Job
    template_name = 'jobs/job.html'
    context_object_name = 'job'
    form_class = JobMessageForm
    extra_context = {
        'title': 'Название вакансии',
        'subtitle': 'Детальная информация касательно вакансии',
    }

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        chat = Chat.objects.create(
            job=self.object,
            type=1,
            user=self.request.user,
            title=self.object.title,
        )
        chat.members.add(self.request.user, self.object.user)

        form = form.save(commit=False)
        form.user = self.request.user
        form.chat = chat
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('job', kwargs={'pk': self.object.pk})


class JobAddView(LoginRequiredMixin, UserCheckTypeEmployerMixin, SuccessMessageMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_message = 'Ваша вакансия была успешно отправлена на проверку. После завершения проверки она станет доступна для просмотра.'
    extra_context = {
        'title': 'Добавление вакансии',
        'subtitle': 'Страница добавления новой вакансии',
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserCheckJobAuthorMixin, SuccessMessageMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_message = 'Вы успешно внесли изменения в вакансию.'
    extra_context = {
        'title': 'Редактирование вакансии',
        'subtitle': 'Страница редактирования вакансии',
    }


class JobDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Job
    success_url = '/profile/jobs'
    success_message = 'Вы успешно удалили вакансию.'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user
        )
