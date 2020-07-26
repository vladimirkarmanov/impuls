import factory
from factory.django import DjangoModelFactory

from register.models import JobPosition


class JobPositionFactory(DjangoModelFactory):
    class Meta:
        model = JobPosition

    name = factory.Faker('job', locale='ru_RU')
