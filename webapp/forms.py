from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class RecordForm(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='Пользователь')
    email = forms.CharField(max_length=30, required=True, label='Email')
    text = forms.CharField(max_length=2000, required=True, label='Text',widget=widgets.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return name
