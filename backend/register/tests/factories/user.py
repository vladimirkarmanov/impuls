import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from register.models import User
from register.tests.factories.job_place import JobPlaceFactory
from register.tests.factories.job_position import JobPositionFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    patronymic = factory.Faker('middle_name', locale='ru_RU')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    experience = fuzzy.FuzzyInteger(0, 100)
    job_place = factory.SubFactory(JobPlaceFactory)
    job_position = factory.SubFactory(JobPositionFactory)
