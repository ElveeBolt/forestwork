from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from settings.models import Country, Specialization
from users.models import User


class ProfileAboutForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя...'
            }
        )
    )
    about = forms.CharField(
        label='О себе:',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите информацию о себе...'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['name', 'about']


class ProfileContactForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        label='Страна:',
        required=False,
        queryset=Country.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите страну...'
            }
        )
    )
    city = forms.CharField(
        label='Город:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите город...'
            }
        )
    )
    phone = forms.CharField(
        label='Телефон:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон...'
            }
        )
    )
    telegram = forms.CharField(
        label='Telegram:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите telegram...'
            }
        )
    )
    whatsapp = forms.CharField(
        label='Whatsapp:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите whatsapp...'
            }
        )
    )
    linkedin = forms.CharField(
        label='LinkedIn:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на linkedin...'
            }
        )
    )
    github = forms.CharField(
        label='GitHub:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на github...'
            }
        )
    )
    website = forms.CharField(
        label='Веб-сайт:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на веб-сайт...'
            }
        )
    )
    portfolio = forms.CharField(
        label='Портфолио:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на портфолио...'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['country', 'city', 'phone', 'telegram', 'whatsapp', 'linkedin', 'github', 'website', 'portfolio']


class ProfileSpecializationForm(forms.ModelForm):
    remote_type = forms.ChoiceField(
        label='Удалённая работа / Офис:',
        required=False,
        choices=User.REMOTE_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите тип работы...'
            }
        )
    )
    exp = forms.ChoiceField(
        label='Опыт работы:',
        required=False,
        choices=User.EXP_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите опыт работы...'
            }
        )
    )
    specialization = forms.ModelChoiceField(
        label='Специализация:',
        required=False,
        queryset=Specialization.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Укажите специализацию...'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['remote_type', 'exp', 'specialization']


class ProfilePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Текущий пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текущий пароль...'
            }
        )
    )
    new_password1 = forms.CharField(
        label='Новый пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите новый пароль...'
            }
        )
    )
    new_password2 = forms.CharField(
        label='Повторите пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль...'
            }
        )
    )
