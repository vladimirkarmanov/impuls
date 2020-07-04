from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer
from django.contrib.auth import login, authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from register.models import User


class UserAuthApiView(APIView):
    permission_classes = [AllowAny]
    username = openapi.Parameter('username', openapi.IN_QUERY,
                                 description="Username parameter.", type=openapi.TYPE_STRING)
    password = openapi.Parameter('password', openapi.IN_QUERY,
                                 description="Password parameter.", type=openapi.TYPE_STRING)

    @swagger_auto_schema(operation_description="Authenticate user.", manual_parameters=[username, password])
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password.'},
                            status=HTTP_400_BAD_REQUEST)
        if '@' in username:
            try:
                user = User.objects.get(email=username.lower())
                username = user.username
            except User.DoesNotExist:
                return Response({'error': 'Invalid Credentials'},
                                status=HTTP_401_UNAUTHORIZED)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials.'},
                            status=HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({'user': UserSerializer(user).data, 'sessionid': request.session.session_key},
                        status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Get user auth data.")
    def get(self, request):
        user = request.user
        return Response({'user': UserSerializer(user).data, 'sessionid': request.session.session_key},
                        status=HTTP_200_OK)
