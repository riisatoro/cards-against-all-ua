from datetime import datetime
import jwt
import pytz

from dateutil.relativedelta import relativedelta
from fastapi import HTTPException
from settings import settings


def encode_jwt(email: str):
    data = {
        'exp': datetime.now(tz=pytz.UTC) + relativedelta(seconds=settings.JWT_ACCESS_EXPIRES_AT),
        'email': email,
    }
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_refresh():
    data = {
        'exp': datetime.now(tz=pytz.UTC) + relativedelta(seconds=settings.JWT_REFRESH_EXPIRES_AT)
    }
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def decode_jwt(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Unauthorized")
