from lib2to3.pytree import Base
from pydantic import BaseModel

from connection import db


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    password: str
