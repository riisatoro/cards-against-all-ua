from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    LargeBinary,
    String,
)
from sqlalchemy.ext.declarative import declared_attr, declarative_base


class __Base(object):
    id =  Column(String, primary_key=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Model = declarative_base(cls=__Base)


class UserModel(Model):
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(LargeBinary, nullable=False)


class UserTokenModel(Model):
    refresh = Column(String, nullable=False)
