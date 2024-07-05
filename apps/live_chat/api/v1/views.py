from rest_framework import generics

from apps.live_chat.api.v1.serializers import MessageSerializer, RoomSerializer
from apps.live_chat.models import Message, Room


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
