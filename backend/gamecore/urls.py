from django.urls import path

from gamecore.views import UserCreateRoomView, UserJoinRoomView, UserLeaveRoomView


urlpatterns = [
    path('create', UserCreateRoomView.as_view(), name='create_game'),
    path('join/', UserJoinRoomView.as_view(), name='join_random_game'),
    path('join/<uuid:room_uuid>/', UserJoinRoomView.as_view(), name='join_concrete_game'),
    path('leave/', UserLeaveRoomView.as_view(), name='leave_game'),
]
