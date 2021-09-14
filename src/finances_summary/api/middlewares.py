import base64
import binascii
from starlette.authentication import (AuthenticationBackend, AuthenticationError,
                                      SimpleUser, UnauthenticatedUser, AuthCredentials,
                                      requires)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from finances_summary import settings


class CustomAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


def get_middlewares() -> [Middleware]:
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
