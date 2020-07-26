import pytest
from django.contrib.auth.models import Group

from .factories.user import UserFactory
from ..models import User


@pytest.mark.django_db
class TestUserModel:
    @pytest.fixture(autouse=True)
    def setup(self):
        UserFactory(first_name='Олег', last_name='Иванов', patronymic='Степанович')

    def test_get_full_name_returns_valid_value(self):
        user = User.objects.first()
        expected = 'Иванов Олег Степанович'
        actual = user.get_full_name()
        assert expected == actual, f'Expected({expected}) is not equal to actual({actual})'

    def test_activate_user_accout_after_email_confirm(self):
        user = User.objects.first()
        user.activate_user_accout_after_email_confirm()
        assert user.is_active is True
        assert user.email_confirmed is True
        assert user.has_usable_password()

    def test_add_user_to_group_listeners(self):
        user = User.objects.first()
        user.add_user_to_group_listeners()
        group = Group.objects.get(name='Слушатели')
        assert user in group.user_set.all(), f'User is not in group {group.name}'

    def test_add_user_to_group_teachers(self):
        user = User.objects.first()
        user.add_user_to_group_teachers()
        group = Group.objects.get(name='Преподаватели')
        assert user in group.user_set.all(), f'User is not in group {group.name}'
