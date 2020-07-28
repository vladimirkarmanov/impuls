import pytest
from django.test import Client

from .factories.user import UserFactory, USER_PASSWORD
from ..models import User


@pytest.fixture
def registered_user() -> User:
    return UserFactory()


@pytest.fixture
def authorized_user(client: Client, registered_user: User) -> User:
    client.login(username=registered_user.username, password=USER_PASSWORD)
    return registered_user
