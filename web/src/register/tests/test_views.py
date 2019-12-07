import pytest
from django.test.client import Client
from django.urls import reverse

from .base_view_mixins import (BaseTestViewMixin,
                               LoginRequiredTestViewMixin,
                               RedirectAuthenticatedTestViewMixin)
from ..models import User, AdditionalUserInfo
from ..views import ListenerSignupView, UserPasswordResetView


@pytest.mark.django_db
class TestListenerSignupView(RedirectAuthenticatedTestViewMixin,
                             BaseTestViewMixin):
    view = ListenerSignupView
    url = '/register/signup/'
    url_name = 'listener_signup'
    template_name = 'register/signup_form.html'
    email_template_name = 'register/account_activation_email.html'
    context = ['form']

    def test_post_request_is_correct(self):
        self.client.post(self.url, {'first_name': 'Джон',
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
            f'User does not have unusable password'


@pytest.mark.django_db
class TestAdditionalInfoView(LoginRequiredTestViewMixin, BaseTestViewMixin):
    url = '/register/signup/paper/'
    url_name = 'additional_info'
    template_name = 'register/additional_info.html'
    context = ['form']

    def test_post_request_is_correct(self):
        self.client.login(username='oleg', password='123456789qwe$')
        user = User.objects.first()
        self.client.post(self.url, {'user': user,
                                    'country': 'Россия',
                                    'region': 'Московская область',
                                    'city': 'Москва',
                                    'address': 'Ул. Пушкина, 12',
                                    'phone': '89991234567',
                                    'mail_index': '807060',
                                    'about': 'Привет, меня зовут ...'})
        info = AdditionalUserInfo.objects.get(user=user)
        assert info.user == user


@pytest.mark.django_db
class TestUserLoginView(RedirectAuthenticatedTestViewMixin, BaseTestViewMixin):
    url = '/register/login/'
    url_name = 'user_login'
    template_name = 'register/login_form.html'
    context = ['form']


@pytest.mark.django_db
class TestUserLogoutView:
    client = Client()
    url = '/register/logout/'
    url_name = 'user_logout'
    context = []

    @pytest.fixture(autouse=True)
    def setup(self):
        User.objects.create_user(
            first_name='Олег', last_name='Иванов',
            patronymic='Степанович', username='oleg',
            email='oleg@mail.ru', password='123456789qwe$'
        )

    def test_view_redirects_after_logout(self):
        self.client.login(username='oleg', password='123456789qwe$')
        response = self.client.get(self.url)
        assert response.status_code == 302

        self.client.login(username='oleg', password='123456789qwe$')
        response = self.client.get(reverse(self.url_name))
        assert response.status_code == 302


@pytest.mark.django_db
class TestUserPasswordResetView(RedirectAuthenticatedTestViewMixin,
                                BaseTestViewMixin):
    view = UserPasswordResetView
    url = '/register/password_reset/'
    url_name = 'password_reset'
    template_name = 'register/password_reset/password_reset_form.html'
    email_template_name = 'register/password_reset/password_reset_email.html'
    context = ['form']


@pytest.mark.django_db
class TestUserPasswordResetDoneView(RedirectAuthenticatedTestViewMixin,
                                    BaseTestViewMixin):
    url = '/register/password_reset/done/'
    url_name = 'password_reset_done'
    template_name = 'register/password_reset/password_reset_done.html'
    context = []


@pytest.mark.django_db
class TestUserPasswordResetCompleteView(RedirectAuthenticatedTestViewMixin,
                                        BaseTestViewMixin):
    url = '/register/password_reset/complete/'
    url_name = 'password_reset_complete'
    template_name = 'register/password_reset/password_reset_complete.html'
    context = []


@pytest.mark.django_db
class TestUserPasswordChangeView(LoginRequiredTestViewMixin,
                                 BaseTestViewMixin):
    url = '/register/password_change/'
    url_name = 'password_change'
    template_name = 'register/password_change/password_change_form.html'
    context = ['form']


@pytest.mark.django_db
class TestUserPasswordChangeDoneView(LoginRequiredTestViewMixin,
                                     BaseTestViewMixin):
    url = '/register/password_change/done/'
    url_name = 'password_change_done'
    template_name = 'register/password_change/password_change_done.html'
    context = []
