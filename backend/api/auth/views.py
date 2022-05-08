from fastapi import APIRouter, HTTPException
from typing import List

from api.auth.schemas import (
    CommonResponseSchema,
    NewUserSchema,
    AccessRefreshTokenSchema,
    UserLoginSchema,
)

from database.collections import User, UserToken
from database.models import UserModel, UserTokenModel
from database.queries import (
    find_in_db,
    insert_to_db,
    update_or_create_in_db,
)
from security.tokens import (
    create_refresh,
    encode_jwt,
)


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)


@router.post('/register', response_model=CommonResponseSchema)
def register(new_user: NewUserSchema):
    user = UserModel(**new_user.dict())
    insert_to_db(User, user)
    return CommonResponseSchema(detail='User have been created successfully')


@router.post('/login', response_model=AccessRefreshTokenSchema)
def login(user_login: UserLoginSchema):
    existed_user = find_in_db(User, user_login)
    if not existed_user:
        raise HTTPException(status_code=404, detail='Invalid credentials')

    refresh_token = create_refresh()
    update_or_create_in_db(UserToken, {'user_id': existed_user['_id']}, {'token': refresh_token})
    return AccessRefreshTokenSchema(access=encode_jwt(existed_user), refresh=refresh_token)


@router.post('/refresh', response_model=AccessRefreshTokenSchema)
def refresh():
    return AccessRefreshTokenSchema(access='ok', refresh='ok')
