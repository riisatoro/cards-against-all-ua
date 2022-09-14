from django.urls import path

from gamesocket.consumers import GameRoomNotifications

websocket_urlpatterns = [
    path('game/<str:room_id>/', GameRoomNotifications.as_asgi()),
]
