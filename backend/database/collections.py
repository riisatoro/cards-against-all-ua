from pydantic import BaseModel

from connection import db


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    password: str
