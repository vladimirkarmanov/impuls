from rest_framework import routers

from chats.api.views import MessageViewSet

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
