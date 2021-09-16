import sys
import uvicorn
from mongoengine import connect
from starlette.applications import Starlette
from finances_summary import settings
from finances_summary.api.middlewares import get_middlewares
from finances_summary.api.routes import all_routes
from finances_summary.settings import MONGO_CONN_URI
from finances_summary.logger import except_handler

# Logging unhandled exceptions.
sys.excepthook = except_handler

# Create middlewares.
middlewares = get_middlewares()

# Create routes.
routes = all_routes()

# Connect MongoEngine.
connect(host=MONGO_CONN_URI)

# Start api.
app = Starlette(debug=True, middleware=middlewares, routes=routes)


if __name__ == '__main__':
    uvicorn.run('app:app',
                host=settings.STARLETTE_HOST,
                port=settings.STARLETTE_PORT,
                reload=settings.STARLETTE_RELOAD,
                ssl_keyfile=settings.STARLETTE_SSL_KEYFILE,
                ssl_certfile=settings.STARLETTE_SSL_CERTFILE)
