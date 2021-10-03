from starlette.authentication import (
    AuthenticationBackend,
    SimpleUser,
    AuthCredentials,
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from finances_summary import settings
from finances_summary.services.authentication import token_valid


class CustomAuthBackend(AuthenticationBackend):
    """Authentication middleware.
    """
    async def authenticate(self, conn):
        token = conn.cookies['token'] if 'token' in conn.cookies else ''
        if token_valid(token):
            return AuthCredentials(["authenticated"]), SimpleUser('')
        return


def get_middlewares() -> list[Middleware]:
    """Get all middlewares.
    :return: List of middlewares.
    :rtype: [Middleware]
    """
    return [
        Middleware(
            CORSMiddleware,
            allow_origins=settings.ALLOWED_ORIGINS,
            allow_credentials=True,
            allow_headers=['Content-Type', 'Authorization'],
            allow_methods=['GET', 'POST', 'OPTIONS'],
        ),
        Middleware(
            SessionMiddleware,
            secret_key=settings.SESSION_MIDDLEWARE_SECRET,
            same_site='none',
            max_age=365 * 24 * 60 * 60,  # 1 year
            https_only=True,
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=CustomAuthBackend(),
        )
    ]
