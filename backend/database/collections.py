from enum import unique
from pydantic import BaseModel
import pymongo

from database.connection import db


User = db['user']
User.create_index([('email', pymongo.ASCENDING)], unique=True)
User.create_index([('username', pymongo.ASCENDING)], unique=True)

RefreshToken = db['refresh']
