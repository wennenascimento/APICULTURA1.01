from django.forms import ModelForm
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'email',
                  'password',
                  ]
