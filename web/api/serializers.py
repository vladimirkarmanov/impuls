from django.contrib.auth.models import Group
from rest_framework import serializers

from register.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'patronymic',
                  'email', 'is_staff', 'is_active', 'date_joined', 'groups')
