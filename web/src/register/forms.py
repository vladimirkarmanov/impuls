from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group

from .models import User, JobPlace, JobPosition


class ListenerSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Повторите пароль'})
    )

    def _get_job_places(self):
        return [(i, job_place)
                for (i, job_place) in enumerate(JobPlace.objects.all(), 1)]

    def _get_job_positions(self):
        return [(i, job_pos)
                for (i, job_pos) in enumerate(JobPosition.objects.all(), 1)]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['experience'].min_value = 0
        self.fields['job_place'].choices = self._get_job_places()
        self.fields['job_position'].choices = self._get_job_positions()

    def save(self, *args, **kwargs):
        user = super().save()
        group, created = Group.objects.get_or_create(name='Слушатели')
        group.user_set.add(user)
        group.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'patronymic', 'username',
                  'email', 'experience',
                  'job_place', 'job_position',
                  'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Фамилия'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Отчество'}),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Логин'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Опыт работы'}),
            'job_place': forms.Select(attrs={'class': 'form-control',
                                             'placeholder': 'Место работы'}),
            'job_position': forms.Select(attrs={'class': 'form-control',
                                                'placeholder': 'Должность'})
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Логин'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'})
    )

    class Meta:
        model = User
        fields = ('username', 'password')
