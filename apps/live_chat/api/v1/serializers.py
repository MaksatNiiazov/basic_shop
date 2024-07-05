from rest_framework import serializers

from apps.live_chat.models import Message, Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'messages']
