from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group

from .models import User, JobPlace, JobPosition, AdditionalUserInfo


class ListenerSignUpForm(UserCreationForm):
    job_place = forms.ModelChoiceField(
        queryset=JobPlace.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'placeholder': 'Место работы'})
    )
    job_position = forms.ModelChoiceField(
        queryset=JobPosition.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'placeholder': 'Должность'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Повторите пароль'})
    )
    country = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Страна'})
    )
    region = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Регион'})
    )
    city = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Город'})
    )
    address = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Адрес'})
    )
    phone = forms.CharField(
        max_length=11,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Телефон'})
    )
    mail_index = forms.IntegerField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Почтовый индекс'})
    )
    about = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'Обо мне'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['experience'].min_value = 0

    def save(self, *args, **kwargs):
        user = super().save()
        group, created = Group.objects.get_or_create(name='Слушатели')
        group.user_set.add(user)
        group.save()
        AdditionalUserInfo.objects.create(
            user=user,
            country=self.cleaned_data['country'],
            region=self.cleaned_data['region'],
            city=self.cleaned_data['city'],
            address=self.cleaned_data['address'],
            phone=self.cleaned_data['phone'],
            mail_index=self.cleaned_data['mail_index'],
            about=self.cleaned_data['about']
        )
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
                                                   'placeholder': 'Опыт работы'})
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
