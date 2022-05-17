from fastapi import APIRouter, Header

from database.queries import get_user


router = APIRouter(
    prefix='/game',
    tags=['Game actions']
)


@router.get('/room')
def get_all_rooms(
    access: str = Header(default=None)
):
    user = get_user(access)
    return []
