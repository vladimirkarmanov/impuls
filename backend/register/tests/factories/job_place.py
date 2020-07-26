import factory
from factory.django import DjangoModelFactory

from register.models import JobPlace


class JobPlaceFactory(DjangoModelFactory):
    class Meta:
        model = JobPlace

    name = factory.Faker('address', locale='ru_RU')
