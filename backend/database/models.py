from typing import Any
from pydantic import BaseModel, validator

from api.auth.schemas import UserSchema
from security.passwords import hash_password
from validators.validators import is_password_length_valid



class UserModel(UserSchema):
    password: str

    _lenth_password = validator('password', allow_reuse=True)(is_password_length_valid)
    _hash_password = validator('password', allow_reuse=True)(hash_password)


class UserTokenModel(BaseModel):
    user_id: Any
    refresh: str
