from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError


def insert_to_db(model, values):
    values = dict(values)
    try:
        model.insert_one(values)
    except DuplicateKeyError:
        raise HTTPException(status_code=422, detail='Username or email already taken')


def find_in_db(model, values):
    values = dict(values)
    return model.find_one(values)


def update_in_db(model, query, values):
    query, values = dict(query), {'$set': dict(values)}
    model.update_one(query, values)


def update_or_create_in_db(model, query, values):
    query, values = dict(query), dict(values)

    existed_user_token = find_in_db(model, dict(query))
    if not existed_user_token:
        insert_to_db(model, {**query, **values})
    else:
        update_in_db(model, query, values)
