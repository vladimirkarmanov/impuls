from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from core.validators import username_regex


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[username_regex]
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')
