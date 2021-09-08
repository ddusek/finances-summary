import os
import logging
import urllib.parse
from datetime import date
from pymongo import MongoClient
from starlette.config import Config
from starlette.datastructures import Secret, CommaSeparatedStrings


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config = Config('.env')


# MongoDB.
MONGO_HOST = config('MONGO_HOST')
MONGO_HOSTNAME = config('MONGO_HOSTNAME')
MONGO_DATABASE = config('MONGO_DATABASE')
MONGO_USERNAME = config('MONGO_USERNAME', cast=Secret)
MONGO_PASSWORD = config('MONGO_PASSWORD', cast=Secret)


# Starlette.
ALLOWED_ORIGINS: list[str] = config('ALLOWED_ORIGINS', cast=CommaSeparatedStrings)
SESSION_MIDDLEWARE_SECRET = config('SESSION_MIDDLEWARE_SECRET', cast=Secret)
STARLETTE_HOST = config('STARLETTE_HOST')
STARLETTE_PORT = config('STARLETTE_PORT', cast=int)
STARLETTE_RELOAD = config('STARLETTE_RELOAD', cast=bool)
STARLETTE_SSL_KEYFILE = config('STARLETTE_SSL_KEYFILE')
STARLETTE_SSL_CERTFILE = config('STARLETTE_SSL_CERTFILE')


# MongoDB connection.
MONGO: MongoClient = MongoClient(
    'mongodb://%s:%s@%s' % (
        urllib.parse.quote_plus(str(MONGO_USERNAME)),
        urllib.parse.quote_plus(str(MONGO_PASSWORD)),
        MONGO_HOSTNAME,
    ),
    serverSelectionTimeoutMS=3000,
)[MONGO_DATABASE]


# Security.
TOKEN_ALGORITHM="ES256K"
TOKEN_SECRET_KEY=config('TOKEN_SECRET_KEY', cast=Secret)


# Logging.
logging.basicConfig(
    filename=f"{ROOT_DIR}/logs/{date.today().isoformat()}.log",
    filemode="a+",
    encoding="utf-8",
    level=logging.WARNING,
)
LOGGER = logging.getLogger(__name__)
