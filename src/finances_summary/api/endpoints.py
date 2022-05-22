from starlette.responses import Response
from starlette.requests import Request
from starlette.authentication import requires
from finances_summary.services.authentication import (register, login,
                                                      is_user_authenticated)
from finances_summary.services.transaction import add, remove, list_
from finances_summary.services.user_summary import total, symbol
from finances_summary.services.cookies import get_user_token
from finances_summary.services.jwt_service import decode_token
from finances_summary.decorators import bind_request


@bind_request
async def register_user(request: Request) -> Response:
    """Register a new user.
    """
    params = await request.json()
    return register(params['username'], params['password'], params['email'])


@bind_request
async def login_user(request: Request) -> Response:
    """Login a user.
    """
    params = await request.json()
    return login(params['login'], params['password'])


@bind_request
async def is_authenticated(request: Request) -> Response:
    """Verify user.
    """
    token = get_user_token()
    return is_user_authenticated(token)


@bind_request
@requires('authenticated')
async def add_transaction(request: Request) -> Response:
    """Add a new transaction.
    """
    params = await request.json()
    return add(**params)


@bind_request
@requires('authenticated')
async def remove_transaction(request: Request) -> Response:
    """Remove a transaction.
    """
    params = await request.json()
    return remove(params['object_id'])


@bind_request
@requires('authenticated')
async def list_transactions(request: Request) -> Response:
    """List user's transactions.
    """
    type_ = request.query_params['type'].upper()
    symbol = request.query_params['symbol'].upper()
    token = get_user_token()
    user = decode_token(token)
    if (user):
        return list_(user, type_, symbol)


@bind_request
@requires('authenticated')
async def user_summary_total(request: Request) -> Response:
    """Summary of user's finances.
    """
    return total()


@bind_request
@requires('authenticated')
async def user_summary_symbol(request: Request) -> Response:
    """Summary of user's specific stock.
    """
    return symbol(request.path_params['symbol'])
