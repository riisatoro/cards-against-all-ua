from fastapi import Header

from database.queries import get_user


def authenticate_user(access: str = Header(default=None)):
    return get_user(access)
