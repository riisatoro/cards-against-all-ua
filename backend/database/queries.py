from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from typing import Union, List


from database.connection import db


def insert_to_db(model, value):
    try:
        model.insert_one(dict(value))
    except DuplicateKeyError as e:
        raise HTTPException(status_code=422, detail='Duplicate fields')
