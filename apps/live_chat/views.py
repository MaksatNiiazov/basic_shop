from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def chat_room(request, room_name):
    return render(request, 'chat/live_chat.html', {
        'room_name': room_name
    })
