from fastapi import APIRouter
from typing import List

from api.auth.schemas import (
    CommonResponseSchema,
    NewUserSchema,
    UserInDBSchema,
)


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)

@router.post('/register', response_model=CommonResponseSchema)
def register(new_user: NewUserSchema):
    user = UserInDBSchema(**new_user.dict())
    return CommonResponseSchema(detail='User have been created successfully')

@router.post('/login')
def login() -> str:
    return 'ok'

@router.post('/refresh')
def refresh() -> str:
    return 'ok'
