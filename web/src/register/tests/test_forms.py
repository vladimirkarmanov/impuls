import pytest

from ..forms import ListenerSignUpForm, AdditionalInfoForm, UserLoginForm


@pytest.mark.django_db
class TestListenerSignUpForm:
    form = ListenerSignUpForm()

    def test_form_has_fields(self):
        expected = {'first_name', 'last_name',
                    'patronymic', 'username',
                    'email', 'experience',
                    'job_place', 'job_position'}
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
