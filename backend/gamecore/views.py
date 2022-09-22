from random import choice

from django.db.models import Count
from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from gamecore.engine import GameEngine

from gamecore.models import RoomModel
from gamecore.serializers import (
    CreateRoomSerializer,
    DefaultResponseSerializer,
    JoinRoomSerializer,
    RoomSerializer,
    UserRoomSerializer,

)
from gamesocket.notifications import notify_room_members
from tasks.tasks import start_new_round


VIEW_TAG = "Game room"


def get_user_room(user):
    return RoomModel.objects.filter(users__in=[user], is_ended=False)


def join_user_to_room(user, uuid=None):
    filters = {"is_ended": False, "users_amount__lt": settings.MAX_ROOM_PLAYER}
    if uuid:
        filters["id"] = uuid
    else:
        filters["is_private"] = False

    available_rooms = RoomModel.objects.annotate(users_amount=Count("users")).filter(
        **filters
    )
    if not available_rooms.exists():
        return False

    room = choice(available_rooms)
    room.users.add(user)
    return room, True


@extend_schema(tags=[VIEW_TAG])
class UserGetCreateRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=CreateRoomSerializer,
        responses={
            200: RoomSerializer,
            401: DefaultResponseSerializer,
        },
    )
    def get(self, request):
        user_room = get_user_room(request.user).first()
        room = RoomSerializer(user_room).data if user_room else {}
        return Response(room, 200)

    @extend_schema(
        request=CreateRoomSerializer,
        responses={
            200: RoomSerializer,
            401: DefaultResponseSerializer,
            422: DefaultResponseSerializer,
        },
    )
    def post(self, request):
        user_in_room = get_user_room(user=request.user)

        if user_in_room.exists():
            return Response({"detail": "You already in game"}, status=422)

        room = CreateRoomSerializer(data=request.POST)
        if not room.is_valid():
            return Response({"detail": "Got invalid data for game room"}, status=422)

        room = room.save()
        room.users.add(self.request.user)

        return Response(RoomSerializer(room).data, status=200)


@extend_schema(tags=[VIEW_TAG])
class UserJoinRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=JoinRoomSerializer,
        responses={
            200: RoomSerializer,
            401: DefaultResponseSerializer,
            422: DefaultResponseSerializer,
        },
    )
    def post(self, request):
        room_uuid = JoinRoomSerializer(request.data).data.get("room_uuid", None)
        user_room = get_user_room(request.user).first()
        if user_room:
            return Response({"detail": "You already in game"}, status=422)

        room, is_joined = join_user_to_room(request.user, uuid=room_uuid)
        if not is_joined:
            return Response(
                {
                    "detail": "Can\t join to room. Either no available rooms left, or you got wrong invitation link."
                },
                status=422,
            )
        
        if GameEngine.try_start_game(room):
            start_new_round.apply_async((room.id,), countdown=settings.FIRST_ROUND_COUNTDOWN)

        group = str(room.id)
        data = RoomSerializer(room).data

        notify_room_members(group, data)
        return Response(RoomSerializer(room).data, status=200)


@extend_schema(tags=[VIEW_TAG])
class UserLeaveRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=JoinRoomSerializer,
        responses={
            200: DefaultResponseSerializer,
            401: DefaultResponseSerializer,
            422: DefaultResponseSerializer,
        },
    )
    def post(self, request):
        user_room = get_user_room(user=request.user)

        if not user_room.exists():
            return Response({"detail": "You don't play in any room"}, status=422)

        user_room = user_room.first()
        user_room.users.remove(request.user)
        
        if not user_room.users.count():
            user_room.delete()
        else:
            group = str(user_room.id)
            data = RoomSerializer(user_room).data
            notify_room_members(group, data)

        return Response({"detail": "You have left from the room"}, status=200)
