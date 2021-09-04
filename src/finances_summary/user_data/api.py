import urllib.parse
from pymongo import MongoClient
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from finances_summary import constants


async def import_data(request: Request) -> JSONResponse:
    """Import records.
    :return: {"success": bool}.
    :rtype: JSONResponse
    """
    return JSONResponse({"success": True})


# Create middlewares.
middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=[
            "https://0.0.0.0:8080",
            "https://localhost:8080",
            "https://127.0.0.1:8080",
        ],
        allow_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        allow_methods=["GET", "POST", "OPTIONS"],
    ),
    Middleware(
        SessionMiddleware,
        secret_key="megasecret",
        same_site="none",
        max_age=365 * 24 * 60 * 60,  # 1 year
        https_only=True,
    ),
]

# Create routes.
routes = [
    Mount(
        "/api/userdata",
        routes=[
            Route("/import", import_data, methods=["POST"]),
        ],
    )
]

# Start api.
app = Starlette(debug=True, middleware=middlewares, routes=routes)


# Connect to MongoDB.
MONGO: MongoClient = MongoClient(
    "mongodb://%s:%s@%s"
    % (
        urllib.parse.quote_plus(constants.MONGO_USERNAME),
        urllib.parse.quote_plus(constants.MONGO_PASSWORD),
        constants.MONGO_HOSTNAME,
    ),
    serverSelectionTimeoutMS=3000,
)["finances-summary"]
