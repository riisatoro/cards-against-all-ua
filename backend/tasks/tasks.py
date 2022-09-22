from celery import shared_task

from gamecore.engine import GameEngine
from gamecore.models import RoomModel


def get_room(room_id: str):
    return RoomModel.objects.get(id=room_id)


@shared_task
def start_new_round(room_id: str):
    room = get_room(room_id)
    
    GameEngine.select_room_leader(room)
    GameEngine.select_question_card(room)
    GameEngine.distribute_answer_cards(room)
    GameEngine.start_new_round(room)

    room.save()


@shared_task
def wait_players_select_answers(room_id):
    ...


@shared_task
def wait_leader_select_best_card(room_id):
    ...
