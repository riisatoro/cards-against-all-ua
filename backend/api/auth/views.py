from tkinter import NE
from fastapi import APIRouter, HTTPException, status

from api.auth.schemas import CommonResponse, NewUser


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)

@router.post('/register', response_model=CommonResponse)
def register(new_user: NewUser):
    return CommonResponse(detail='User have been created successfully')

@router.post('/login')
def login() -> str:
    return 'ok'

@router.post('/refresh')
def refresh() -> str:
    return 'ok'
