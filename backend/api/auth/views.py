from fastapi import APIRouter, HTTPException
from typing import List

from api.auth.schemas import (
    CommonResponseSchema,
    NewUserSchema,
    UserInDBSchema,
    AccessRefreshTokenSchema,
    UserLoginSchema,
)

from database.collections import User
from database.queries import (
    insert_to_db,
    find_in_db,
)


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)


@router.post('/register', response_model=CommonResponseSchema)
def register(new_user: NewUserSchema):
    user = UserInDBSchema(**new_user.dict())
    insert_to_db(User, user)
    return CommonResponseSchema(detail='User have been created successfully')


@router.post('/login', response_model=AccessRefreshTokenSchema)
def login(user_login: UserLoginSchema):
    existed_user = find_in_db(User, user_login)
    if not existed_user:
        raise HTTPException(status_code=404, detail='Invalid credentials')
    return AccessRefreshTokenSchema(access='ok', refresh='ok')


@router.post('/refresh', response_model=AccessRefreshTokenSchema)
def refresh():
    return AccessRefreshTokenSchema(access='ok', refresh='ok')
