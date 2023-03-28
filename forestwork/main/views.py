from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from jobs.models import Job
from jobs.forms import JobSearchForm
from users.models import User


# Create your views here.
class IndexView(FormMixin, TemplateView):
    template_name = 'main/index.html'
    form_class = JobSearchForm
    extra_context = {
        'title': 'ForestWork',
        'subtitle': 'Сервис поиска работы и кандидатов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_list'] = Job.objects.filter(status=1)[:5]
        context['employer_list'] = User.objects.filter(type=1)[:5]
        context['developer_list'] = User.objects.filter(type=0)[:5]
        context['job_count'] = Job.objects.all().count()
        return context