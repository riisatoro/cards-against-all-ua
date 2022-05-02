from pydantic import BaseModel, validator

from validators.validators import (
    is_alphanumeric,
    is_password_length_valid,
    is_username_length_valid,
)


class CommonResponse(BaseModel):
    detail: str


class User(BaseModel):
    username: str
    email: str

    _alphanumeric_username = validator('username', allow_reuse=True)(is_alphanumeric)
    _lenth_username = validator('username', allow_reuse=True)(is_username_length_valid)


class UserInDB(User):
    password: str


class NewUser(User):
    password: str
    repeat_password: str

    _lenth_password = validator('password', allow_reuse=True)(is_password_length_valid)

    @validator('repeat_password')
    def repeat_password_valid(cls, v):
        if cls.password != v:
            raise ValueError('Passwords don\'t match')
        return v
