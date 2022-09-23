from django.conf import settings
from celery import shared_task

from gamecore.engine import GameEngine
from gamecore.queries import get_room
from gamecore.serializers import RoomSerializer
from gamesocket.notifications import notify_room_members


@shared_task
def wait_leader_select_best_card(room_id):
    room = get_room(room_id)

    notify_room_members(room_id, RoomSerializer(room).data)

    start_new_round.apply_async((room_id,), countdown=settings.FIRST_ROUND_COUNTDOWN)


@shared_task
def wait_players_select_answers(room_id):
    room = get_room(room_id)

    notify_room_members(room_id, RoomSerializer(room).data)


    wait_leader_select_best_card.apply_async(
        (room_id,), countdown=settings.ROOM_WAIT_TIME
    )


@shared_task
def start_new_round(room_id: str):
    room = get_room(room_id)
    GameEngine.start_new_round(room)

    notify_room_members(room_id, RoomSerializer(room).data)

    print('--- START NEW ROUND ---')
    # wait_players_select_answers.apply_async(
    #     (room_id,), countdown=settings.ROOM_WAIT_TIME
    # )
