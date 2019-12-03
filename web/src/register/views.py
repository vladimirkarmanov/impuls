from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView

from .forms import (ListenerSignUpForm,
                    UserLoginForm,
                    AdditionalInfoForm)
from .services import *
from .tokens import account_activation_token


class ListenerSignupView(CreateView):
    form_class = ListenerSignUpForm
    template_name = 'register/signup_form.html'
    success_url = reverse_lazy('listener_signup_url')

    def form_valid(self, form):
        user = User.objects.create_user(**form.cleaned_data, is_active=False)
        user.set_unusable_password()
        current_site = get_current_site(self.request)
        user.email_user(
            'Активируйте свой аккаунт',
            render_to_string('register/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
        )
        return HttpResponse('Перейдите по ссылке из письма на вашем почтовом'
                            ' ящике, чтобы активировать свой аккаунт')


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        activate_user_accout_after_email_confirm(user)
        add_user_to_group_listeners(user)
        return render(request, 'register/success_activate_account.html')
    else:
        return HttpResponse('Срок действия этой ссылки истек!')


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
