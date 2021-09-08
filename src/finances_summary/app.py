import uvicorn
from starlette.applications import Starlette
from finances_summary import settings
from finances_summary.middlewares import get_middlewares
from finances_summary.routes import all_routes

# Create middlewares.
middlewares = get_middlewares()

# Create routes.
routes = all_routes()

# Start api.
app = Starlette(debug=True, middleware=middlewares, routes=routes)

if __name__ == '__main__':
    uvicorn.run('app:app',
                host=settings.STARLETTE_HOST,
                port=settings.STARLETTE_PORT,
                reload=settings.STARLETTE_RELOAD,
                ssl_keyfile=settings.STARLETTE_SSL_KEYFILE,
                ssl_certfile=settings.STARLETTE_SSL_CERTFILE)
