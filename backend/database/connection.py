from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


__db_url = getenv('DATABASE_URL')

if not __db_url:
    __db_url = f'postgresql://{0}:{1}@{2}:{3}/{4}'
    __db_url.format(
        getenv('POSTGRES_USER'),
        getenv('POSTGRES_PASSWORD'),
        getenv('POSTGRES_HOST'),
        getenv('POSTGRES_PORT'),
        getenv('POSTGRES_DB'),
    )

engine = create_engine(__db_url)

session = sessionmaker(engine)()
