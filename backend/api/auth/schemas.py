from pydantic import BaseModel, validator

from security.passwords import hash_password
from validators.validators import (
    is_alphanumeric,
    is_email_valid,
    is_password_length_valid,
    is_passwords_matched,
    is_username_length_valid,
)


class CommonResponseSchema(BaseModel):
    detail: str


class UserSchema(BaseModel):
    username: str
    email: str

    _alphanumeric_username = validator('username', allow_reuse=True)(is_alphanumeric)
    _lenth_username = validator('username', allow_reuse=True)(is_username_length_valid)
    _valid_email = validator('email', allow_reuse=True)(is_email_valid)


class UserInDbSchema(UserSchema):
    password: str

    _lenth_password = validator('password', allow_reuse=True)(is_password_length_valid)


class NewUserSchema(UserInDbSchema):
    repeat_password: str

    _matched_password = validator('repeat_password', allow_reuse=True)(is_passwords_matched)


class UserLoginSchema(BaseModel):
    email: str
    password: str

    _hash_password = validator('password', allow_reuse=True)(hash_password)


class AccessTokenSchema(BaseModel):
    access: str

    _access_str = validator('access', allow_reuse=True)(lambda v: str(v))


class RefreshTokenSchema(BaseModel):
    refresh: str

    _refresh_str = validator('refresh', allow_reuse=True)(lambda v: str(v))


class AccessRefreshTokenSchema(BaseModel):
    access: str
    refresh: str

    _access_str = validator('access', allow_reuse=True)(lambda v: str(v))
    _refresh_str = validator('refresh', allow_reuse=True)(lambda v: str(v))
