from pydantic import BaseModel

from connection import db


User = db['user']
