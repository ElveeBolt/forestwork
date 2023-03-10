from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm


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
    country = forms.CharField(
        label='Страна:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну...'
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
