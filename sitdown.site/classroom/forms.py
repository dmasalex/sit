from django import forms
from .models import Schoolboy
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SchoolboyForm(forms.ModelForm):
    class Meta:
        model = Schoolboy
        fields = [
            'name', 'phone', 'date_of_birth',
            'photo', 'comment', 'classroom',
            'gender', 'requirement', 'energy', 'height'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'input-file'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'classroom': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'requirement': forms.Select(attrs={'class': 'form-control'}),
            'energy': forms.CheckboxInput(),
            'height': forms.NumberInput(attrs={'class': 'form-control'})
        }
