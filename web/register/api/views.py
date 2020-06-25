from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from register.api.serializers import UserSerializer
from register.models import User


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List of all users'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Get one user'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create a user'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Remove a user'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update a user'))
@method_decorator(name='partial_update',
                  decorator=swagger_auto_schema(operation_description='Partial update a user.'))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    search_query = openapi.Parameter('search_query', openapi.IN_QUERY, required=True,
                                     description='Search query.', type=openapi.TYPE_STRING)

    @action(detail=False, methods=['get'])
    @swagger_auto_schema(operation_description='Get users by search query.', manual_parameters=[search_query])
    def users_by_search_query(self, request):
        if search_query := request.query_params.get('search_query'):
            users = User.objects \
                .exclude(id=request.user.id) \
                .filter(Q(first_name__icontains=search_query) |
                        Q(last_name__icontains=search_query) |
                        Q(patronymic__icontains=search_query))

            serializer = UserSerializer(users, many=True)
            self.paginate_queryset(users)
            return self.get_paginated_response(serializer.data)
        else:
            return Response({'error': 'Please provide query param: search_query'}, status=HTTP_400_BAD_REQUEST)
