from django import forms
from django.forms import HiddenInput
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user',
            'x',
            'y',
            'pkgid',
            'pid',
            'count',
            'whid',
            'truckid',
            'status',
            'email'
        ]
        widgets = {'user': HiddenInput(),
                   'x': forms.TextInput(attrs={'class': 'form-control'}),
                   'y': forms.TextInput(attrs={'class': 'form-control'}),
                   'pkgid': HiddenInput(),
                   'pid': forms.TextInput(attrs={'class': 'form-control'}),
                   'count': forms.TextInput(attrs={'class': 'form-control'}),
                   'whid': HiddenInput(),
                   'truckid': HiddenInput(),
                   'status': HiddenInput(),
                   'email': forms.TextInput(attrs={'class': 'form-control'})}
