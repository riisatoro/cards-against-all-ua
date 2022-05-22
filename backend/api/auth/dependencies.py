from fastapi import Header, HTTPException

from database.queries import get_user


def authenticate_user(access: str = Header(default=None)):
    user = get_user(access)
    if not user:
        raise HTTPException(status_code=403, detail='Unauthorized')
    return user
