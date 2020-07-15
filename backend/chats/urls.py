from django.urls import path
from rest_framework import routers

from .views import ChatsView, MessagesView, CreateChatView

urlpatterns = [
    path('', ChatsView.as_view(), name='chats'),
    path('<int:chat_id>/', MessagesView.as_view(), name='messages'),
    path('create/<int:user_id>/', CreateChatView.as_view(), name='create_chat'),
]
