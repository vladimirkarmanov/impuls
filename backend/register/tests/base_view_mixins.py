import pytest
from django.test import Client
from django.urls import reverse

from ..models import User


class BaseTestViewMixin:
    view = None
    url = None
    url_name = None
    template_name = None
    email_template_name = None
    context = None

    def test_view_url_exists_at_desired_location(self, client: Client):
        response = client.get(self.url)
        assert response.status_code == 200

    def test_view_url_accessible_by_name(self, client: Client):
        response = client.get(reverse(self.url_name))
        assert response.status_code == 200

    def test_view_uses_correct_template(self, client: Client):
        response = client.get(self.url)
        assert self.template_name in [t.name for t in response.templates], \
            f'{self.template_name} is not in response'

        if self.email_template_name:
            expected = self.email_template_name
            actual = self.view.email_template_name
            assert expected == actual, \
                f'{self.email_template_name} is not in response'

    def test_view_returns_valid_context(self, client: Client):
        response = client.get(self.url)
        difference = [x for x in self.context if x not in response.context]
        assert len(difference) == 0, \
            f'{difference} is not in response.context'


@pytest.mark.usefixtures('authorized_user')
class LoginRequiredTestViewMixin(BaseTestViewMixin):

    def test_view_redirects_anonymous_user(self, client: Client):
        client.logout()
        response = client.get(self.url)
        assert response.status_code == 302


class RedirectAuthenticatedTestViewMixin(BaseTestViewMixin):
    def test_view_redirects_auth_user_to_main_page(self, client: Client, authorized_user: User):
        response = client.get(self.url)
        assert response.status_code == 301
