from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN

from chats.api.serializers import MessageSerializer
from chats.models import Message, Chat


@method_decorator(name='list', decorator=swagger_auto_schema(operation_description='List of all messages'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_description='Get one message'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_description='Create a message'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description='Remove a message'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_description='Update a message'))
@method_decorator(name='partial_update',
                  decorator=swagger_auto_schema(operation_description='Partial update a message.'))
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    chat_id = openapi.Parameter('chat_id', openapi.IN_QUERY, required=True,
                                description='Chat_id param.', type=openapi.TYPE_INTEGER)

    @action(detail=False, methods=['get'])
    @swagger_auto_schema(operation_description='Get messages by chat id.', manual_parameters=[chat_id])
    def messages_by_chat(self, request):
        if chat_id := request.query_params.get('chat_id'):
            try:
                chat = Chat.objects.get(id=chat_id)
                messages = chat.messages.all()

                if request.user in chat.members.all():
                    chat.messages.unreaded().exclude(author=request.user).update(is_readed=True)

                serializer = MessageSerializer(messages, many=True)
                self.paginate_queryset(messages)
                return self.get_paginated_response(serializer.data)
            except Chat.DoesNotExist:
                return Response({'error': f'Not found'}, status=HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Please provide query param: chat_id'}, status=HTTP_400_BAD_REQUEST)
