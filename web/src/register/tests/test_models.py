import pytest

from ..models import User, AdditionalUserInfo, JobPosition, JobPlace


@pytest.mark.django_db
class TestUserModel:
    @pytest.fixture(autouse=True)
    def setup(self):
        User.objects.create(username='oleg',
                            password='123456789qwe$')

    def test_fields_max_length(self):
        user = User.objects.first()
        assert user._meta.get_field('first_name').max_length == 30
        assert user._meta.get_field('last_name').max_length == 30
        assert user._meta.get_field('patronymic').max_length == 30
        assert user._meta.get_field('email').max_length == 70

    def test_fields_has_valid_default_values(self):
        user = User.objects.first()
        assert user._meta.get_field('email_confirmed').default is False
        assert user._meta.get_field('experience').default == 0


@pytest.mark.django_db
class TestAdditionalUserInfoModel:
    @pytest.fixture(autouse=True)
    def setup(self):
        user = User.objects.create(username='oleg',
                                   password='123456789qwe$')
        AdditionalUserInfo.objects.create(user=user,
                                          region='Московская область',
                                          city='Москва')

    def test_fields_max_length(self):
        info = AdditionalUserInfo.objects.first()
        assert info._meta.get_field('country').max_length == 30
        assert info._meta.get_field('region').max_length == 50
        assert info._meta.get_field('city').max_length == 30
        assert info._meta.get_field('address').max_length == 120
        assert info._meta.get_field('phone').max_length == 11
        assert info._meta.get_field('mail_index').max_length == 6
        assert info._meta.get_field('about').max_length == 500

    def test_fields_has_valid_default_values(self):
        info = AdditionalUserInfo.objects.first()
        assert info._meta.get_field('country').default == 'Россия'


@pytest.mark.django_db
class TestJobPlaceModel:
    @pytest.fixture(autouse=True)
    def setup(self):
        JobPlace.objects.create(name='Школа')

    def test_fields_max_length(self):
        job_place = JobPlace.objects.first()
        assert job_place._meta.get_field('name').max_length == 150


@pytest.mark.django_db
class TestJobPositionModel:
    @pytest.fixture(autouse=True)
    def setup(self):
        JobPosition.objects.create(name='Учитель')

    def test_fields_max_length(self):
        job_place = JobPosition.objects.first()
        assert job_place._meta.get_field('name').max_length == 150
