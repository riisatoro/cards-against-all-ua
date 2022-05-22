from lib2to3.pytree import Base
from os import getenv

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = getenv('SECRET_KEY')
    JWT_ALGORITHM: str = 'HS256'
    JWT_ACCESS_EXPIRES_AT: int = 60 * 60
    JWT_REFRESH_EXPIRES_AT: int = 60 * 60 * 24

    ROOM_WAIT_TIME: int = 120
    MINIMAL_ROOM_PLAYERS: int = 3


settings = Settings()
