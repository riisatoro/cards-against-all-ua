from sqlalchemy import select

from database.connection import session
from database.models import UserModel
from security.passwords import hash_password


def __prepare_user_model(model):
    model.password = hash_password(model.password)
    return model


def save_model(model):
    if type(model) == UserModel:
        model = __prepare_user_model(model)

    try:
        session.add(model)
        session.commit()
        return model
    except:
        session.rollback()
        return None


def select_objects(model, **kwargs):
        query = select(model).filter_by(**kwargs)
        return session.execute(query).all()


def select_single_object(model, **kwargs):
    results = select_objects(model, **kwargs)
    
    if not results:
        return None

    if len(results) > 1:
        raise ValueError('Found multiple objects for this query')

    return results[0][0]
