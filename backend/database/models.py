from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    String,
)
from sqlalchemy.ext.declarative import declared_attr, declarative_base


class __Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id =  Column(String, primary_key=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


Base = declarative_base(cls=__Base)
