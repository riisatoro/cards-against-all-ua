from random import choice

from django.conf import settings
from django.db.models import Count

from gamecore.models import RoomModel


def get_room(room_id: str):
    return RoomModel.objects.get(id=room_id)


def get_user_room(user):
    return RoomModel.objects.filter(users__in=[user], is_ended=False).first()


def create_room(user, is_private=False):
    room = RoomModel.objects.create(is_private=is_private)
    room.users.set([user])
    return room


def get_free_room(room_id=None):
    room = (
        RoomModel.objects.annotate(user_amount=Count("users"))
        .filter(
            **{
                "is_ended": False,
                "user_amount__lt": settings.MAX_ROOM_PLAYER,
                "is_private": bool(room_id),
            }
        )
        .order_by("-user_amount")
    )

    if room_id:
        room = room.filter(id=room_id)

    return room.first()
