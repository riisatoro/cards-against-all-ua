from random import choice

from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from gamecore.models import GameState
from gamecore.queries import get_user_room, create_room, get_free_room
from gamecore.serializers import (
    RoomSerializer,
)
from gamecore.schemas import (
    CreateRoomSchema,
    JoinRoomSchema,
    DefaultResponseSchema,
)
from gamesocket.notifications import notify_room_members
from gamecore.responses import ViewResponses
from tasks.tasks import start_new_round


VIEW_TAG = "Game room"


@extend_schema(tags=[VIEW_TAG])
class GetCreateRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=CreateRoomSchema,
        responses={200: RoomSerializer, 401: DefaultResponseSchema},
    )
    def get(self, request):
        room = get_user_room(request.user)
        return Response(RoomSerializer(room).data, 200)

    def post(self, request):
        room = get_user_room(request.user)
        if room:
            return Response(ViewResponses.already_in_game, 422)

        room = create_room(user=request.user)
        return Response(RoomSerializer(room).data, 201)


@extend_schema(tags=[VIEW_TAG])
class JoinRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=JoinRoomSchema,
        responses={
            200: RoomSerializer,
            401: DefaultResponseSchema,
            422: DefaultResponseSchema,
        },
    )
    def post(self, request):
        room = get_free_room(request.POST.get("room_uuid"))
        if not room or room.users.count() >= settings.MAX_ROOM_PLAYER:
            return Response(ViewResponses.room_join_error, 422)

        if get_user_room(request.user):
            return Response(ViewResponses.already_in_game, 200)

        room.users.add(request.user)
        request.user.cards.clear()
        request.user.answer_cards.clear()

        if (
            room.room_state == GameState.WAIT_FOR_NEW_PLAYERS
            and room.users.count() >= settings.MIN_ROOM_PLAYERS
        ):
            room.room_state = GameState.WAIT_FOR_NEW_ROUND
            room.save()

            start_new_round.apply_async(
                (str(room.id),), countdown=settings.FIRST_ROUND_COUNTDOWN
            )

        room_data = RoomSerializer(room).data
        notify_room_members(str(room.id), room_data)
        return Response(room_data, 200)


@extend_schema(tags=[VIEW_TAG])
class LeaveRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        responses={
            200: DefaultResponseSchema,
            401: DefaultResponseSchema,
            422: DefaultResponseSchema,
        },
    )
    def post(self, request):
        user_room = get_user_room(request.user)

        if not user_room:
            return Response(ViewResponses.user_not_in_room, status=422)

        user_room.users.remove(request.user)
        request.user.cards.clear()
        request.user.answer_cards.clear()

        if not user_room.users.count():
            user_room.delete()
        else:
            notify_room_members(str(user_room.id), RoomSerializer(user_room).data)

        return Response(ViewResponses.user_left_successfully, status=200)


@extend_schema(tags=[VIEW_TAG])
class SelectAnswerCards(APIView):
    @extend_schema
    def post(self, request):
        room = get_user_room(request.user)
        return Response({}, 200)


class SelectBestAnswer(APIView):
    ...
