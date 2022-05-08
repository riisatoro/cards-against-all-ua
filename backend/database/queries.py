from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError


def insert_to_db(model, values):
    try:
        model.insert_one(dict(values))
    except DuplicateKeyError:
        raise HTTPException(status_code=422, detail='Username or email already taken')


def find_in_db(model, values):
    return model.find_one(dict(values))
