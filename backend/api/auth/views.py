from fastapi import APIRouter, HTTPException

from api.auth.schemas import (
    CommonResponseSchema,
    NewUserSchema,
    AccessRefreshTokenSchema,
    RefreshTokenSchema,
    UserInDbSchema,
    UserLoginSchema,
)
from database.models import UserModel, UserTokenModel
from database.queries import (
    save_model,
    select_single_object,
)
from security.passwords import hash_password
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
    user = UserInDbSchema(**new_user.dict())

    user = UserModel(**user.dict())

    user = save_model(user)
    if not user:
        raise HTTPException(status_code=400, detail='Username or email already exists.')

    return CommonResponseSchema(detail='User have been created successfully')


@router.post('/login', response_model=AccessRefreshTokenSchema)
def login(user_login: UserLoginSchema):
    user = select_single_object(UserModel, email=user_login.email)
    password = hash_password(user_login.password)

    if not user or user.password != password:
        raise HTTPException(status_code=404, detail='Invalid credentials')
    
    access_token = encode_jwt(user.email)
    refresh_token = create_refresh()    
    user_token = select_single_object(UserTokenModel, user=user)

    if not user_token:
        user_token = UserTokenModel(user=user, refresh=refresh_token)
        user_token = save_model(user_token)
    else:
        user_token.refresh = refresh_token
        user_token = save_model(user_token)

    return AccessRefreshTokenSchema(access=access_token, refresh=user_token.refresh)


@router.post('/refresh', response_model=AccessRefreshTokenSchema)
def refresh(token: RefreshTokenSchema):
    user_token = select_single_object(UserTokenModel, refresh=token.refresh)
    if not user_token or not decode_jwt(user_token.refresh):
        raise HTTPException(status_code=403, detail='Invalid credentials')

    access_token = encode_jwt(user_token.user.email)
    user_token.refresh = create_refresh()
    save_model(user_token)
    
    return AccessRefreshTokenSchema(access=access_token, refresh=user_token.refresh)
