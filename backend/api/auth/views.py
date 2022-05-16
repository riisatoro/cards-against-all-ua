from bson import encode
from fastapi import APIRouter, HTTPException
from typing import List

from api.auth.schemas import (
    CommonResponseSchema,
    NewUserSchema,
    AccessRefreshTokenSchema,
    RefreshTokenSchema,
    UserLoginSchema,
)

# from database.collections import User, UserToken
# from database.models import UserModel, UserTokenModel
# from database.queries import (
#     find_in_db,
#     insert_to_db,
#     update_in_db,
#     update_or_create_in_db,
# )
from security.tokens import (
    create_refresh,
    decode_jwt,
    encode_jwt,
)


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)


@router.post('/register', response_model=CommonResponseSchema)
def register(new_user: NewUserSchema):
    # user = UserModel(**new_user.dict())
    # insert_to_db(User, user)
    # return CommonResponseSchema(detail='User have been created successfully')
    return 'ok'


@router.post('/login', response_model=AccessRefreshTokenSchema)
def login(user_login: UserLoginSchema):
    # existed_user = find_in_db(User, user_login)
    # if not existed_user:
    #     raise HTTPException(status_code=404, detail='Invalid credentials')

    # refresh_token = create_refresh()
    # update_or_create_in_db(UserToken, {'_id': existed_user['_id']}, {'refresh': refresh_token})
    # return AccessRefreshTokenSchema(access=encode_jwt(existed_user), refresh=refresh_token)
    return 'ok'


@router.post('/refresh', response_model=AccessRefreshTokenSchema)
def refresh(token: RefreshTokenSchema):
    # user_token = find_in_db(UserToken, token)
    # print(user_token)
    # if not user_token or not decode_jwt(user_token['refresh']):
    #     raise HTTPException(status_code=403, detail='Invalid credentials')

    # user = find_in_db(User, {'_id': user_token["_id"]})
    # refresh_token = create_refresh()
    # update_in_db(UserToken, {'_id': user['_id']},{'refresh': refresh_token})
    # return AccessRefreshTokenSchema(access=encode_jwt(user), refresh=refresh_token)
    return 'ok'
