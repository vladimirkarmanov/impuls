from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import (ListenerSignUpForm,
                    UserLoginForm,
                    AdditionalInfoForm)


class ListenerSignupView(CreateView):
    form_class = ListenerSignUpForm
    template_name = 'register/signup_form.html'
    success_url = reverse_lazy('listener_signup_url')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        if form.cleaned_data['is_paper']:
            return redirect(reverse('additional_info_url'))
        return redirect(self.success_url)


class AdditionalInfoView(CreateView):
    form_class = AdditionalInfoForm
    template_name = 'register/additional_info.html'
    success_url = reverse_lazy('listener_signup_url')

    def form_valid(self, form):
        additional_info = form.save(commit=False)
        additional_info.user = self.request.user
        additional_info.save()
        return redirect(self.success_url)


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'register/login_form.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user_login_url')
