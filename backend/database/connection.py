import os

from pymongo.mongo_client import MongoClient


__mongo_uri = 'mongodb://{}:{}@{}:{}'.format(
    os.getenv('MONGO_INITDB_ROOT_USERNAME'),
    os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
    os.getenv('MONGO_DATABASE_HOST'),
    os.getenv('MONGO_DATABASE_PORT'),
)

__db_cluster = MongoClient(__mongo_uri)

db = __db_cluster[os.getenv('MONGO_DATABASE_NAME')]
