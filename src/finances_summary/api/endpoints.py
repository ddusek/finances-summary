from starlette.responses import Response
from starlette.requests import Request
from finances_summary.services.authentication import register, login, verify_token
from finances_summary.services.transaction import add, remove, list_
from finances_summary.services.user_summary import total, symbol


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


async def verify_user_token(request: Request) -> Response:
    """Logout a user.
    """
    cookies = request.cookies
    token: str = cookies['token'] if 'token' in cookies else ''
    return verify_token(token)


async def add_transaction(request: Request) -> Response:
    """Add a new transaction.
    """
    params = await request.json()
    return add(**params)
    # return add(params['date'], params['record_type'], params['symbol'], params['amount'],
    #            params['price_per_unit'])


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


async def user_summary_total(request: Request) -> Response:
    """Summary of user's finances.
    """
    return total()


async def user_summary_symbol(request: Request) -> Response:
    """Summary of user's specific stock.
    """
    return symbol(request.path_params['symbol'])

