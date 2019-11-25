import pytest

from django.contrib.auth.models import Group

from ..forms import ListenerSignUpForm, AdditionalInfoForm, UserLoginForm
from ..models import User


@pytest.mark.django_db
class TestListenerSignUpForm:
    form = ListenerSignUpForm()

    def test_form_has_fields(self):
        expected = {'first_name', 'last_name',
                    'patronymic', 'username',
                    'email', 'experience',
                    'job_place', 'job_position',
                    'password1', 'password2'}
        actual = set(self.form.fields)
        difference = expected - actual
        assert len(difference) == 0, \
            f'Expected fields are: {expected} \n' \
            f'Actual fields are: {actual} \n' \
            f'Fields {difference} not in form'

    def test_experience_field_has_valid_min_value(self):
        expected = 0
        actual = self.form.fields['experience'].min_value
        assert expected == actual, \
            f'Expected field min_value == {expected} \n' \
            f'Actual field min_value == {actual}'

    def test_custom_fields_has_valid_required_property(self):
        assert not self.form.fields['job_place'].required
        assert not self.form.fields['job_position'].required
        assert not self.form.fields['is_paper'].required
        assert self.form.fields['password1'].required
        assert self.form.fields['password2'].required

    def test_save_method(self):
        form = ListenerSignUpForm(
            data={'first_name': 'Олег',
                  'last_name': 'Молчанов',
                  'patronymic': 'Анатольевич',
                  'username': 'oleg',
                  'email': 'oleg@mail.ru',
                  'experience': 5,
                  'job_place': None,
                  'job_position': None,
                  'password1': '123456789qwe$',
                  'password2': '123456789qwe$'}
        )
        form.save()
        user = User.objects.get(username='oleg')
        group = Group.objects.get(name='Слушатели')
        assert user.username == 'oleg'
        assert group.name == 'Слушатели'
        assert user in group.user_set.all()


class TestAdditionalInfoForm:
    form = AdditionalInfoForm()

    def test_form_has_fields(self):
        expected = {'country', 'region', 'city', 'address',
                    'phone', 'mail_index', 'about'}
        actual = set(self.form.fields)
        difference = expected - actual
        assert len(difference) == 0, \
            f'Expected fields are: {expected} \n' \
            f'Actual fields are: {actual} \n' \
            f'Fields {difference} not in form'


class TestUserLoginForm:
    form = UserLoginForm()

    def test_form_has_fields(self):
        expected = {'username', 'password'}
        actual = set(self.form.fields)
        difference = expected - actual
        assert len(difference) == 0, \
            f'Expected fields are: {expected} \n' \
            f'Actual fields are: {actual} \n' \
            f'Fields {difference} not in form'
