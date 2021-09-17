from starlette.responses import Response
from starlette.requests import Request
from finances_summary.services.authentication import register, login, logout
from finances_summary.services.transaction import add, remove, list_


async def register_user(request: Request) -> Response:
    """Register a new user.
    """
    params = await request.json()
    return register(params['username'], params['password'], params['email'])


async def login_user(request: Request) -> Response:
    """Login a user.
    """
    params = await request.json()
    return login(params['login'], params['password'])


async def logout_user(request: Request) -> Response:
    """Logout a user.
    """
    params = await request.json()
    return logout(params['token'], params['username'])


async def add_transaction(request: Request) -> Response:
    """Add a new transaction.
    """
    params = await request.json()
    return add(params['date'], params['record_type'], params['symbol'], params['amount'],
               params['price_per_unit'])


async def remove_transaction(request: Request) -> Response:
    """Remove a transaction.
    """
    params = await request.json()
    return remove(params['object_id'])


async def list_transactions(request: Request) -> Response:
    """List user's transactions.
    """
    type_ = request.query_params['type']
    symbol = request.query_params['symbol']
    return list_(type_, symbol)
