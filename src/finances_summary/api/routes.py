from starlette.routing import Route, Mount
from finances_summary.api.endpoints import register_user, login_user, logout_user


def _user_routes() -> list[Route]:
    """Routes for user.
    """
    return [
        Route('/register', register_user, methods=['POST']),
        Route('/login', login_user, methods=['POST']),
        Route('/logout', logout_user, methods=['POST']),
    ]


def _stock_routes() -> list[Route]:
    """Routes for stocks.
    """
    return []


def all_routes() -> list[Mount]:
    """Get all routes for api.
    """
    return [Mount('/api/user', routes=_user_routes()),
            Mount('/api/stock', routes=_stock_routes())]
