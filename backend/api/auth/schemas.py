from pydantic import BaseModel, validator

from operations.passwords import hash_password
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


class UserInDBSchema(UserSchema):
    password: str

    _lenth_password = validator('password', allow_reuse=True)(is_password_length_valid)
    _hash_password = validator('password', allow_reuse=True)(hash_password)


class NewUserSchema(UserSchema):
    password: str
    repeat_password: str

    _lenth_password = validator('password', allow_reuse=True)(is_password_length_valid)
    _matched_password = validator('repeat_password', allow_reuse=True)(is_passwords_matched)


class UserLoginSchema(BaseModel):
    email: str
    password: str

    _hash_password = validator('password', allow_reuse=True)(hash_password)


class AccessTokenSchema(BaseModel):
    access: str


class RefreshTokenSchema(BaseModel):
    refresh: str


class AccessRefreshTokenSchema(BaseModel):
    access: str
    refresh: str
