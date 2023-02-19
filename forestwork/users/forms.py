from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
    password = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Логин:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин...'
            }
        )
    )
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
    type = forms.IntegerField(
        label='Тип аккаунта:',
        required=True,
        widget=forms.RadioSelect(
            choices=User.PROFILE_CHOICES,
            attrs={'class': 'form-check-input'}
        )
    )
    email = forms.CharField(
        label='E-mail:',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail...'
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль...'
            }
        )
    )
    password2 = forms.CharField(
        label='Повторите пароль:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль...'
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'name', 'type', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется")

        return email
