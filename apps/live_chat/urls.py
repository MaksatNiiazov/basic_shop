from django.urls import path, include
from apps.live_chat.views import chat_room

urlpatterns = [
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('api/v1/', include('apps.live_chat.api.v1.urls'))
]
