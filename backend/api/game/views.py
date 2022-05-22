from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends, HTTPException

from api.auth.dependencies import authenticate_user
from database.models import (
    RoomModel,
    UserModel,
    UserRoomModel,
)
from database.queries import (
    save_model,
    select_single_object,
)
from settings import settings


router = APIRouter(
    prefix='/game',
    tags=['Game actions']
)


@router.get('')
def get_user_room(
    user: UserModel = Depends(authenticate_user),
):
    return 'ok'


@router.post('/create')
def create_room(
    is_private: bool = False,
    user: UserModel = Depends(authenticate_user),
):
    user_room = select_single_object(UserRoomModel, user_id=user.id)
    if user_room:
        raise HTTPException(status=422, detail='You already in game')

    room = RoomModel(
        is_private=is_private,
        round_end_time=datetime.now() + relativedelta(seconds=settings.ROOM_WAIT_TIME)
    )
    room = save_model(user_room)

    user_room = UserRoomModel(room_id=room.id, user_id=user.id)
    user_room = save_model(user_room)

    return 'ok'


@router.post('/join')
def join_room(
    user: UserModel = Depends(authenticate_user),
    room_id: str = None,
):
    return 'ok'


@router.post('/leave')
def leave_room(
    user: UserModel = Depends(authenticate_user),
    room_id: str = None,
):
    return 'ok'
