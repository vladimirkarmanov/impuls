from rest_framework.serializers import ModelSerializer

from register.models import JobPlace, JobPosition


class JobPlaceSerializer(ModelSerializer):
    class Meta:
        model = JobPlace
        fields = '__all__'


class JobPositionSerializer(ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'
