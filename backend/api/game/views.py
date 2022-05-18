from fastapi import APIRouter, Depends

from api.auth.dependencies import authenticate_user
from database.models import UserModel


router = APIRouter(
    prefix='/game',
    tags=['Game actions']
)


@router.get('/room')
def get_all_rooms(user: UserModel = Depends(authenticate_user)):
    return []
