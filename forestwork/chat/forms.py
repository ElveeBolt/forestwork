from django import forms
from .models import Message


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