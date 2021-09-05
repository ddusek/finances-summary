import urllib.parse
import uvicorn
from pymongo import MongoClient
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from finances_summary import settings


async def import_data(request: Request) -> JSONResponse:
    """Import records.
    :return: {"success": bool}.
    :rtype: JSONResponse
    """
    return JSONResponse({'success': True})


# Create middlewares.
middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_headers=['Content-Type', 'Authorization'],
        allow_methods=['GET', 'POST', 'OPTIONS'],
    ),
    Middleware(
        SessionMiddleware,
        secret_key='megasecret',
        same_site='none',
        max_age=365 * 24 * 60 * 60,  # 1 year
        https_only=True,
    ),
]

# Create routes.
routes = [
    Mount(
        '/api/userdata',
        routes=[
            Route('/import', import_data, methods=['POST']),
        ],
    )
]

# Start api.
app = Starlette(debug=True, middleware=middlewares, routes=routes)

# Connect to MongoDB.
MONGO: MongoClient = MongoClient(
    'mongodb://%s:%s@%s' % (
        urllib.parse.quote_plus(str(settings.MONGO_USERNAME)),
        urllib.parse.quote_plus(str(settings.MONGO_PASSWORD)),
        settings.MONGO_HOSTNAME,
    ),
    serverSelectionTimeoutMS=3000,
)['finances-summary']

if __name__ == '__main__':
    uvicorn.run('app:app',
                host=settings.STARLETTE_HOST,
                port=settings.STARLETTE_PORT,
                reload=settings.STARLETTE_RELOAD,
                ssl_keyfile=settings.STARLETTE_SSL_KEYFILE,
                ssl_certfile=settings.STARLETTE_SSL_CERTFILE)
