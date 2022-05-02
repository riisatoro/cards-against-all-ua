from lib2to3.pytree import Base
from pydantic import BaseModel


class CommonResponse(Base):
    detail: str


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    password: str


class NewUser(User):
    password: str
    repeat_password: str
