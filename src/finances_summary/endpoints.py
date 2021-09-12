from starlette.responses import Response
from starlette.requests import Request
from mongoengine import connect
from finances_summary.authentication import register, login, logout
from finances_summary.settings import _mongo_conn_uri


async def register_user(request: Request) -> Response:
    """Register a new user.
    """
    params = await request.json()
    return register(params['username'], params['password'], params['email'])


async def login_user(request: Request) -> Response:
    """Register a new user.
    """
    params = await request.json()
    return login(params['login'], params['password'])


async def logout_user(request: Request) -> Response:
    """Register a new user.
    """
    params = await request.json()
    return logout(params['token'], params['username'])
