from datetime import datetime
from enums import CardsEnum
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    ForeignKey,
    LargeBinary,
    String,
    Text,
    Enum,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import relationship


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

    refresh = relationship('UserTokenModel', back_populates='user')


class UserTokenModel(Model):
    id = Column(String, ForeignKey('usermodel.id'), primary_key=True)
    refresh = Column(String, nullable=False)

    user = relationship('UserModel', back_populates='refresh')


class CardsModel(Model):
    text = Column(Text, nullable=False)
    card_type = Column(Enum(CardsEnum), nullable=False)


class RoomModel(Model):
    is_started = Column(Boolean, default=False)
    is_ended = Column(Boolean, default=False)

    round_number = Column(Integer, default=0)
    round_end_time = Column(DateTime, nullable=False)

    leader = Column(String, ForeignKey('usermodel.id'), nullable=True)
    question_card = Column(String, ForeignKey('cardsmodel.id'), nullable=True)
    funny_card = Column(String, ForeignKey('cardsmodel.id'), nullable=True)


class UserRoomModel(Model):
    __table_args__ = (
        UniqueConstraint('user_id', 'room_id'),
    )

    user_id = Column(String, ForeignKey('usermodel.id'), nullable=True)
    room_id = Column(String, ForeignKey('roommodel.id'), nullable=True)

    user_score = Column(Integer, default=0)
    answer_card = Column(String, ForeignKey('cardsmodel.id'))


class UserRoomCardsModel(Model):
    __table_args__ = (
        UniqueConstraint('user_room_id', 'card_id'),
    )

    user_room_id = Column(String, ForeignKey('userroommodel.id'), nullable=False)
    card_id = Column(String, ForeignKey('cardsmodel.id'), nullable=False)
