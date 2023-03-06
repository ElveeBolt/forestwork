from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, LoginView, LogoutView, PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, FormView
from .forms import LoginForm, SignupForm, UserContactForm, UserAboutForm, UserPasswordForm, UserForgotPasswordForm, \
    UserSetForgotPasswordForm
from jobs.models import Job
from .models import User
from .utils import send_email_for_verify, send_email_for_forgot_password
from django.http import Http404


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
    ordering = ['-date_joined']
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


class DeveloperListView(ListView):
    model = User
    paginate_by = settings.RESULTS_PER_PAGE
    template_name = 'users/developers.html'
    context_object_name = 'developers'
    ordering = ['-date_joined']
    extra_context = {
        'title': 'Разработчики',
        'subtitle': 'Список разработчиков',
    }

    def get_queryset(self):
        return User.objects.filter(type=0)


class DeveloperDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user_info'
    extra_context = {
        'title': 'Информация о пользователе',
        'subtitle': 'Дополнительная информация о разработчике',
    }


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/index.html'
    extra_context = {
        'title': 'Профиль',
        'subtitle': 'Страница профиля'
    }


class ProfileJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'profile/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-date_joined']
    extra_context = {
        'title': 'Мои вакансии',
        'subtitle': 'Опубликованные вами вакансии',
    }

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


class ProfileMainUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserAboutForm
    template_name = 'profile/main.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfileContactsUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserContactForm
    template_name = 'profile/contacts.html'
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordForm
    template_name = 'profile/password.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'title': 'Редактирование профиля',
        'subtitle': 'Страница редактирования профиля',
    }


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
    }


class UserForgotPasswordView(PasswordResetView):
    email_template_name = 'emails/forgot_password.html'
    form_class = UserForgotPasswordForm
    template_name = 'users/forgot_password.html'
    success_url = reverse_lazy('forgot_password_send')
    extra_context = {
        'title': 'Сброс пароля',
        'subtitle': 'В случае, если вы забыли пароль вы можете его восстановить.',
    }


class UserForgotPasswordSendView(TemplateView):
    template_name = 'users/forgot_password_send.html'
    extra_context = {
        'title': 'Спасибо',
        'subtitle': 'Отправлены инструкции для восстановления пароля',
    }


class UserForgotPasswordVerifyView(PasswordResetConfirmView):
    model = User
    form_class = UserSetForgotPasswordForm
    template_name = 'users/forgot_password_form.html'
    success_url = reverse_lazy('forgot_password_verify_success')
    extra_context = {
        'title': 'Сброс пароля',
        'subtitle': 'Заполните форму ниже для того чтобы сбросить пароль',
    }


class UserForgotPasswordVerifySuccessView(TemplateView):
    template_name = 'users/forgot_password_verify_success.html'
    extra_context = {
        'title': 'Наши поздравления',
        'subtitle': 'Сброс пароля',
    }


class UserForgotPasswordVerifyInvalidView(TemplateView):
    template_name = 'users/forgot_password_verify_invalid.html'
    extra_context = {
        'title': 'Токен не найден',
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
            return redirect('signup_verify_success')

        raise Http404('Verify Token is invalid')


class UserVerifySuccessView(TemplateView):
    template_name = 'users/signup_verify_success.html'
    extra_context = {
        'title': 'Наши поздравления',
        'subtitle': 'Подтверждение email адреса',
    }


class UserLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
