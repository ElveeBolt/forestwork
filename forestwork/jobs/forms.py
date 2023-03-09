from django import forms
from .models import Job
from settings.models import Country


class JobForm(forms.ModelForm):
    title = forms.CharField(
        label='Название вакансии:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название...'
            }
        )
    )
    description = forms.CharField(
        label='Описание:',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание к вакансии...',
                'rows': 5
            }
        )
    )
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
                'placeholder': 'Укажите город...'
            }
        )
    )
    salary = forms.IntegerField(
        label='Зарплата:',
        required=False,
        help_text='Учтите, зарплата указывается в долларах.',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    comment = forms.CharField(
        label='Комментарий:',
        required=False,
        help_text='Укажите дополнительную информацию, которая так или иначе относится к вашему предложению.',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация...',
                'rows': 5
            }
        )
    )

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['user']
