from starlette.routing import Route, Mount
from finances_summary.api.endpoints import (
    register_user, login_user, logout_user, add_transaction, list_transactions,
    remove_transaction, user_summary_total, user_summary_symbol)


def _user_routes() -> list[Route]:
    """Routes for user.
    """
    return [
        Route('/register', register_user, methods=['POST']),
        Route('/login', login_user, methods=['POST']),
        Route('/logout', logout_user, methods=['POST']),
    ]


def _transaction_routes() -> list[Route]:
    """Routes for user transactions.
    """
    return [
        Route('/add', add_transaction, methods=['POST']),
        Route('/remove', remove_transaction, methods=['DELETE']),
        Route('/list', list_transactions, methods=['GET']),
        Mount(  # type: ignore
            '/summary',
            routes=[
                Route('/total', user_summary_total, methods=['POST']),
                Route('/symbol/{symbol:str}', user_summary_symbol, methods=['POST'])
            ]),
    ]


def _stock_routes() -> list[Route]:
    """Routes for stocks.
    """
    return []


def all_routes() -> list[Mount]:
    """Get all routes for api.
    """
    return [
        Mount('/api',
              routes=[
                  Mount('/user', routes=_user_routes()),
                  Mount('/transaction', routes=_transaction_routes()),
                  Mount('/stock', routes=_stock_routes())
              ])
    ]
