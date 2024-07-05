from django.urls import path

from .views import MessageList, RoomList

urlpatterns = [
    path('messages/', MessageList.as_view(), name='message-list'),
    path('rooms/', RoomList.as_view(), name='room-list'),
]
