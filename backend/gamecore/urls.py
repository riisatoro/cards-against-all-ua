from django.urls import path

from gamecore.views import (
    GetCreateRoomView,
    JoinRoomView,
    LeaveRoomView,
)


urlpatterns = [
    path('', GetCreateRoomView.as_view(), name='game'),
    path('join/', JoinRoomView.as_view(), name='join_game'),
    path('leave/', LeaveRoomView.as_view(), name='leave_game'),
]
