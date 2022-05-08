from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError


def insert_to_db(model, value):
    try:
        model.insert_one(dict(value))
    except DuplicateKeyError:
        raise HTTPException(status_code=422, detail='Username or email already taken')
