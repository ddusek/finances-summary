import os
import urllib.parse
from starlette.config import Config
from starlette.datastructures import Secret, CommaSeparatedStrings

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config = Config('.env')

# MongoDB.
MONGO_HOST = config('MONGO_HOST')
MONGO_PORT = 27017
MONGO_HOSTNAME = config('MONGO_HOSTNAME')
MONGO_DATABASE = config('MONGO_DATABASE')
MONGO_USERNAME = config('MONGO_USERNAME', cast=Secret)
MONGO_PASSWORD = config('MONGO_PASSWORD', cast=Secret)

# Connect with hostname - used for connections from Docker.
MONGO_CONN_URI = 'mongodb://%s:%s@%s/%s?authSource=admin' % (
    urllib.parse.quote_plus(str(MONGO_USERNAME)),
    urllib.parse.quote_plus(str(MONGO_PASSWORD)),
    MONGO_HOSTNAME,
    MONGO_DATABASE
)

# Connect with host (IP address) - used for connections outside of Docker.
MONGO_CONN_URI_WITH_HOST = 'mongodb://%s:%s@%s/%s?authSource=admin' % (
    urllib.parse.quote_plus(str(MONGO_USERNAME)),
    urllib.parse.quote_plus(str(MONGO_PASSWORD)),
    MONGO_HOST,
    MONGO_DATABASE
)

# Starlette.
ALLOWED_ORIGINS: list[str] = config('ALLOWED_ORIGINS', cast=CommaSeparatedStrings)
SESSION_MIDDLEWARE_SECRET = config('SESSION_MIDDLEWARE_SECRET', cast=Secret)
STARLETTE_HOST = config('STARLETTE_HOST')
STARLETTE_PORT = config('STARLETTE_PORT', cast=int)
STARLETTE_RELOAD = config('STARLETTE_RELOAD', cast=bool)
STARLETTE_SSL_KEYFILE = config('STARLETTE_SSL_KEYFILE')
STARLETTE_SSL_CERTFILE = config('STARLETTE_SSL_CERTFILE')

# JWT Token.
JWT_ALGORITHM = "ES256K"
JWT_PRIVATE_KEY_PATH = f'{ROOT_DIR}/secrets/private-jwt.pem'
JWT_PUBLIC_KEY_PATH = f'{ROOT_DIR}/secrets/public-jwt.pem'
