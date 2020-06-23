from rest_framework import serializers

from chats.models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'
