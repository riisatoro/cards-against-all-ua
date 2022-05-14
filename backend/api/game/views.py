from typing import Optional
from fastapi import APIRouter, Header

from api.auth.decorators import login_required

router = APIRouter(
    prefix='/game',
    tags=['Game actions']
)

@router.get('/room')
@login_required
def get_all_rooms(*args, **kwargs):
    return []
