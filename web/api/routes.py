from rest_framework import routers

from chats.api.views import MessageViewSet
from register.api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet)
