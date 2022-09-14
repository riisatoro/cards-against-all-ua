from django.urls import re_path

from gamesocket.consumers import GameRoomNotifications

websocket_urlpatterns = [
    re_path(r'game/$', GameRoomNotifications.as_asgi()),
]
