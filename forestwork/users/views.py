from django.http import Http404
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetConfirmView, LoginView, LogoutView, PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import FormMixin
from .forms import LoginForm, SignupForm, UserForgotForm, UserSetForgotPasswordForm
from .models import User
from chat.models import Chat
from chat.forms import JobOfferForm
from jobs.models import Job
from .utils import send_email_for_verify


# Create your views here.
def index(request):
    # TODO: add functionality users list page.

    context = {
        'title': 'Список пользователей',
        'subtitle': 'Все пользователи сайта'
    }
    return render(request, 'users/index.html', context=context)


class EmployerListView(ListView):
    model = User
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'users/employers.html'
    context_object_name = 'employers'
    extra_context = {
        'title': 'Работодатели',
        'subtitle': 'Список работодателей и компаний',
    }

    def get_queryset(self):
        return User.objects.filter(type=1)


class EmployerDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user_info'
    extra_context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о работодателе или компании',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.filter(user=self.object, status=1)
        return context


class DeveloperListView(ListView):
    model = User
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'users/developers.html'
    context_object_name = 'developers'
    extra_context = {
        'title': 'Разработчики',
        'subtitle': 'Список разработчиков',
    }

    def get_queryset(self):
        return User.objects.filter(type=0)


class DeveloperDetailView(FormMixin, DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user_info'
    form_class = JobOfferForm
    success_url = '/profile/chats'
    extra_context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о разработчике',
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['current_user'] = self.request.user
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = Job.objects.get(id=request.POST.get('job'))
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        chat = Chat.objects.create(
            job=self.object,
            type=0,
            user=self.request.user,
            title=self.object.title,
        )
        chat.members.add(self.request.user, self.object.user)

        form = form.save(commit=False)
        form.user = self.request.user
        form.chat = chat
        form.save()

        form_valid = super().form_valid(form)

        return form_valid


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
    }


class UserForgotView(PasswordResetView):
    email_template_name = 'emails/forgot.html'
    form_class = UserForgotForm
    template_name = 'users/forgot.html'
    success_url = reverse_lazy('forgot_send')
    extra_context = {
        'title': 'Сброс пароля',
        'subtitle': 'В случае, если вы забыли пароль вы можете его восстановить.',
    }


class UserForgotSendView(TemplateView):
    template_name = 'users/forgot_send.html'
    extra_context = {
        'title': 'Спасибо',
        'subtitle': 'Отправлены инструкции для восстановления пароля',
    }


class UserForgotVerifyView(PasswordResetConfirmView):
    model = User
    form_class = UserSetForgotPasswordForm
    template_name = 'users/forgot_verify.html'
    success_url = reverse_lazy('forgot_success')
    extra_context = {
        'title': 'Сброс пароля',
        'subtitle': 'Заполните форму ниже для того чтобы сбросить пароль',
    }


class UserForgotSuccessView(TemplateView):
    template_name = 'users/forgot_success.html'
    extra_context = {
        'title': 'Наши поздравления',
        'subtitle': 'Сброс пароля',
    }


class UserSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signup_activate')
    extra_context = {
        'title': 'Регистрация профиля',
        'subtitle': 'Создайте профиль для того, чтобы использовать преимущества ForestWork',
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        send_email_for_verify(self.request, user)
        return redirect('signup_activate')


class UserActivateView(TemplateView):
    template_name = 'users/signup_activate.html'
    extra_context = {
        'title': 'Подтвердите свой e-mail',
        'subtitle': 'Подтвердите свою учётную запись',
    }


class UserVerifyView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('signup_success')

        raise Http404('Verify Token is invalid')


class UserVerifySuccessView(TemplateView):
    template_name = 'users/signup_success.html'
    extra_context = {
        'title': 'Наши поздравления',
        'subtitle': 'Подтверждение email адреса',
    }


class UserLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
