from django import forms
from .models import *

class SendSmsForm(forms.Form):
    message = forms.CharField(max_length=255, label="Текст сообщения")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Номера")

class DelSmsForm(forms.Form):
    message = forms.CharField(max_length=255, label="Текст сообщения")