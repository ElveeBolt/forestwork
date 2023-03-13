from django.views.generic import TemplateView
from jobs.models import Job
from users.models import User


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'ForestWork',
        'subtitle': 'Сервис поиска работы и кандидатов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_list'] = Job.objects.filter(status=1)[:5]
        context['employer_list'] = User.objects.filter(type=1)[:5]
        context['developer_list'] = User.objects.filter(type=0)[:5]
        return context