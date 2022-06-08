from django.urls import path

from gamecore.views import (
    UserGetCreateRoomView,
    UserJoinRoomView,
    UserLeaveRoomView,
)


urlpatterns = [
    path('', UserGetCreateRoomView.as_view(), name='game'),
    path('join/', UserJoinRoomView.as_view(), name='join_game'),
    path('leave/', UserLeaveRoomView.as_view(), name='leave_game'),
]
