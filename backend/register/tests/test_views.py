import pytest
from django.test.client import Client
from django.urls import reverse

from .base_view_mixins import (LoginRequiredTestViewMixin,
                               RedirectAuthenticatedTestViewMixin)
from ..models import User, AdditionalUserInfo
from ..views import ListenerSignupView, UserPasswordResetView


@pytest.mark.django_db
class TestListenerSignupView(RedirectAuthenticatedTestViewMixin):
    view = ListenerSignupView
    url = '/register/signup/'
    url_name = 'register:listener_signup'
    template_name = 'register/signup_form.html'
    email_template_name = 'register/account_activation_email.html'
    context = ['form']

    def test_post_request_is_correct(self, client: Client):
        client.post(self.url, {'first_name': 'Джон',
                               'last_name': 'Джонсон',
                               'patronymic': 'Робертович',
                               'username': 'john',
                               'email': 'john@mail.ru',
                               'experience': 5})
        user = User.objects.get(username='john')
        assert user.is_active is False, \
            f'user.is_active is not False'
        assert user.email_confirmed is False, \
            f'user.email_confirmed is not False'
        assert not user.has_usable_password(), \
            f'User does not have usable password'


@pytest.mark.django_db
class TestAdditionalInfoView(LoginRequiredTestViewMixin):
    url = '/register/signup/paper/'
    url_name = 'register:additional_info'
    template_name = 'register/additional_info.html'
    context = ['form']

    def test_post_request_is_correct(self, client: Client, authorized_user: User):
        client.post(self.url, {'user': authorized_user,
                               'country': 'Россия',
                               'region': 'Московская область',
                               'city': 'Москва',
                               'address': 'Ул. Пушкина, 12',
                               'phone': '89991234567',
                               'mail_index': '807060',
                               'about': 'Привет, меня зовут ...'})
        info = AdditionalUserInfo.objects.get(user=authorized_user)
        assert info.user == authorized_user


@pytest.mark.django_db
class TestUserLoginView(RedirectAuthenticatedTestViewMixin):
    url = '/register/login/'
    url_name = 'register:user_login'
    template_name = 'register/login_form.html'
    context = ['form']


@pytest.mark.django_db
class TestUserLogoutView:
    url = '/register/logout/'
    url_name = 'register:user_logout'
    context = []

    def test_view_redirects_after_logout(self, client: Client, registered_user: User):
        # logout with url
        client.login(username=registered_user.username, password=registered_user.password)
        response = client.get(self.url)
        assert response.status_code == 302

        # logout with url_name
        client.login(username=registered_user.username, password=registered_user.password)
        response = client.get(reverse(self.url_name))
        assert response.status_code == 302


@pytest.mark.django_db
class TestUserPasswordResetView(RedirectAuthenticatedTestViewMixin):
    view = UserPasswordResetView
    url = '/register/password_reset/'
    url_name = 'register:password_reset'
    template_name = 'register/password_reset/password_reset_form.html'
    email_template_name = 'register/password_reset/password_reset_email.html'
    context = ['form']


@pytest.mark.django_db
class TestUserPasswordResetDoneView(RedirectAuthenticatedTestViewMixin):
    url = '/register/password_reset/done/'
    url_name = 'register:password_reset_done'
    template_name = 'register/password_reset/password_reset_done.html'
    context = []


@pytest.mark.django_db
class TestUserPasswordResetCompleteView(RedirectAuthenticatedTestViewMixin):
    url = '/register/password_reset/complete/'
    url_name = 'register:password_reset_complete'
    template_name = 'register/password_reset/password_reset_complete.html'
    context = []


@pytest.mark.django_db
class TestUserPasswordChangeView(LoginRequiredTestViewMixin):
    url = '/register/password_change/'
    url_name = 'register:password_change'
    template_name = 'register/password_change/password_change_form.html'
    context = ['form']


@pytest.mark.django_db
class TestUserPasswordChangeDoneView(LoginRequiredTestViewMixin):
    url = '/register/password_change/done/'
    url_name = 'register:password_change_done'
    template_name = 'register/password_change/password_change_done.html'
    context = []
