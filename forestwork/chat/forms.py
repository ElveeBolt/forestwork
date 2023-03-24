from django import forms
from .models import Message
from jobs.models import Job


class JobMessageForm(forms.ModelForm):
    message = forms.CharField(
        label='Текст сообщения:',
        required=True,
        help_text='Укажите свои сильные стороны, навыки и почему именно вы являетесь хорошим кандидатом',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст сообщения...',
                'rows': 5
            }
        )
    )

    class Meta:
        model = Message
        fields = ['message', ]


class AnswerMessageForm(forms.ModelForm):
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст сообщения...',
                'rows': 1
            }
        )
    )

    class Meta:
        model = Message
        fields = ['message', ]


class JobOfferForm(forms.ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job'].queryset = Job.objects.filter(user=current_user, status=1)

    job = forms.ModelChoiceField(
        label='Вакансия:',
        queryset=None,
        required=True,
        help_text='Выберите вакансию которую хотите предложить кандидату',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'placeholder': 'Выберите вакансию...',
            }
        )
    )
    message = forms.CharField(
        label='Текст сообщения:',
        required=True,
        help_text='Укажите основную информацию касательно вакансии или работы которую предлагаете.',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст сообщения...',
                'rows': 5
            }
        )
    )

    class Meta:
        model = Message
        fields = ['message', 'job']