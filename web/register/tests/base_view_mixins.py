import pytest
from django.test import Client
from django.urls import reverse

from ..models import User


def login(func):
    def inner(*args, **kwargs):
        BaseTestViewMixin.login()
        func(*args, **kwargs)
        return func

    return inner


class BaseTestViewMixin:
    client = Client()
    view = None
    url = None
    url_name = None
    template_name = None
    email_template_name = None
    context = None

    @pytest.fixture(autouse=True)
    def setup(self):
        User.objects.create_user(
            first_name='Олег', last_name='Иванов',
            patronymic='Степанович', username='oleg',
            email='oleg@mail.ru', password='123456789qwe$'
        )

    @classmethod
    def login(cls):
        cls.client.login(username='oleg', password='123456789qwe$')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        assert response.status_code == 200

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse(self.url_name))
        assert response.status_code == 200

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        assert self.template_name in [t.name for t in response.templates], \
            f'{self.template_name} is not in response'

        if self.email_template_name:
            expected = self.email_template_name
            actual = self.view.email_template_name
            assert expected == actual, \
                f'{self.email_template_name} is not in response'

    def test_view_returns_valid_context(self):
        response = self.client.get(self.url)
        difference = [x for x in self.context if x not in response.context]
        assert len(difference) == 0, \
            f'{difference} is not in response.context'


class LoginRequiredTestViewMixin(BaseTestViewMixin):
    @login
    def test_view_url_exists_at_desired_location(self):
        super().test_view_url_exists_at_desired_location()

    @login
    def test_view_url_accessible_by_name(self):
        super().test_view_url_accessible_by_name()

    @login
    def test_view_uses_correct_template(self):
        super().test_view_uses_correct_template()

    @login
    def test_view_returns_valid_context(self):
        super().test_view_returns_valid_context()

    def test_view_redirects_anonymous_user(self):
        response = self.client.get(self.url)
        assert response.status_code == 302


class RedirectAuthenticatedTestViewMixin(BaseTestViewMixin):
    @login
    def test_view_redirects_auth_user_to_main_page(self):
        response = self.client.get(self.url)
        assert response.status_code == 302
