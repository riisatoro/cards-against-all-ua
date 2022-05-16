from database.connection import session

def save_model(model):
    session.add(model)
    session.commit()
    return model
    
