from starlette.routing import Route, Mount
from starlette.responses import JSONResponse, Response
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED


async def import_data(request: Request) -> JSONResponse:
    """Import records.
    """
    if 1 == 1:
        return JSONResponse(content={'success': False}, status_code=HTTP_401_UNAUTHORIZED)
    return Response(status_code=HTTP_401_UNAUTHORIZED)


def _user_routes() -> [Route]:
    """Routes for specific user.
    """
    return [
        Route('/import', import_data, methods=['POST']),
    ]


def _stock_routes() -> [Route]:
    """Routes for stocks.
    """
    return []


def all_routes() -> [Mount]:
    """Get all routes for api.
    """
    return [Mount('/api/user', routes=_user_routes()),
            Mount('api/stock', routes=_stock_routes())]
