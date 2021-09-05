from starlette.config import Config
from starlette.datastructures import Secret, CommaSeparatedStrings

config = Config('.env')
print(config('MONGO_HOST', default="nope"))

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
