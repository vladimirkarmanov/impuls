import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from register.models import AdditionalUserInfo
from register.tests.factories.user import UserFactory


class AdditionalUserInfoFactory(DjangoModelFactory):
    class Meta:
        model = AdditionalUserInfo

    user = factory.SubFactory(UserFactory)
    country = factory.Faker('country', locale='ru_RU')
    region = factory.Faker('region', locale='ru_RU')
    city = factory.Faker('city', locale='ru_RU')
    address = factory.Faker('address', locale='ru_RU')
    phone = factory.Faker('phone_number', locale='ru_RU')
    mail_index = fuzzy.FuzzyInteger(100000, 999999)
    about = fuzzy.FuzzyText(length=500)
