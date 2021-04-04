from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, JobPlace, JobPosition, AdditionalUserInfo


class ListenerSignUpForm(UserCreationForm):
    job_place = forms.ModelChoiceField(
        label='Место работы',
        queryset=JobPlace.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    job_position = forms.ModelChoiceField(
        label='Должность',
        queryset=JobPosition.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['experience'].min_value = 0
        del self.fields['password1']
        del self.fields['password2']

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'patronymic', 'username',
                  'email', 'experience',
                  'job_place', 'job_position')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'})
        }


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalUserInfo
        fields = ('country', 'region', 'city', 'address',
                  'phone', 'mail_index', 'about')

        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_index': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control',
                                           'style': 'resize: none;'})
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')
