from unittest import result
from sqlalchemy import select

from database.connection import session

def save_model(model):
    session.add(model)
    session.commit()
    return model
    
def select_objects(model, **kwargs):
        query = select(model).filter_by(**kwargs)
        return session.execute(query).all()

def select_single_object(model, **kwargs):
    results = select_objects(model, **kwargs)
    if len(result) > 1:
        raise ValueError('Found multiple objects for this query')
    
    return results[0]
