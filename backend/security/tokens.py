from datetime import date, datetime
import jwt
import os
import pytz

from dateutil.relativedelta import relativedelta

from database.collections import User


ALGORITHM = 'HS256'
SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ACCESS_EXPIRES_AT = int(os.getenv('JWT_ACCESS_EXPIRES_AT'))
JWT_REFRESH_EXPIRES_AT = int(os.getenv('JWT_ACCESS_EXPIRES_AT'))


def encode_jwt(user: User):
    data = {
        'exp': datetime.now(tz=pytz.UTC) + relativedelta(seconds=JWT_ACCESS_EXPIRES_AT),
        'user': user.email,
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh():
    data = {
        'exp': datetime.now(tz=pytz.UTC) + relativedelta(seconds=JWT_REFRESH_EXPIRES_AT)
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
