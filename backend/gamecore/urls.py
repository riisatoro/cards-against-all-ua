from django.urls import path

from gamecore.views import UserCreateRoomView, UserJoinRoomView, UserLeaveRoomView


urlpatterns = [
    path('create', UserCreateRoomView.as_view()),
    path('join/', UserJoinRoomView.as_view()),
    path('join/<uuid:room_uuid>/', UserJoinRoomView.as_view()),
    path('leave/', UserLeaveRoomView.as_view()),
]
