from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ListenerSignUpForm, UserLoginForm


class ListenerSignupView(CreateView):
    form_class = ListenerSignUpForm
    template_name = 'register/signup_form.html'
    success_url = reverse_lazy('listener_signup_url')


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'register/login_form.html'
