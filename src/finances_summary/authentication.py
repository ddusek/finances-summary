from datetime import datetime, timedelta
from jwt import encode
from argon2 import PasswordHasher
from argon2.exceptions import (
    HashingError,
    VerificationError,
    VerifyMismatchError,
    InvalidHash,
)
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_200_OK
from finances_summary.models.authentication import JwtUserModel
from finances_summary.models.mongo.user import User
from finances_summary.settings import LOGGER, TOKEN_ALGORITHM, TOKEN_SECRET_KEY

# def authorized(func: callable):
#     def decorator(*args, **kwargs):
#         if request.user.is_authenticated:
#             return func
#         else:
#             return Response(status_code=HTTP_401_UNAUTHORIZED)
#     return decorator


def _is_email(login: str) -> bool:
    """Check if login is email or username.
    """
    return "@" in login


def _rehash_password(user: User, password: str) -> None:
    """hash password again if Argon2 parameters change.
    """
    try:
        pwd_hasher = PasswordHasher()
        new_hashed_pwd = pwd_hasher.hash(password)
        user.password = new_hashed_pwd
        user.update()

    except HashingError as err:
        LOGGER.exception(err)


def _generate_token(data: JwtUserModel, expiration: timedelta = timedelta(365)) -> bytes:
    """Generate JWT token.
    """
    expire = datetime.now() + expiration
    data.update({"exp": expire})
    encoded_jwt = encode(data, TOKEN_SECRET_KEY, algorithm=TOKEN_ALGORITHM)
    return encoded_jwt


def _find_user(login) -> User:
    """Find user either by email or username.
    """
    if _is_email(login):
        return User.objects(email=login).first()
    return User.objects(username=login).first()


def register(username: str, password: str, email: str) -> Response:
    """Register a new user.
    """
    if not username:
        raise ValueError("cannot register user, didnt get username")
    if not password:
        raise ValueError("cannot register user, didnt get password")
    if not email:
        raise ValueError("cannot register user, didnt get email")

    if _find_user(email) is not None:
        return Response(status_code=HTTP_409_CONFLICT)
    try:
        pwd_hasher = PasswordHasher()
        user = User().create_new(username, email, pwd_hasher.hash(password))
        user.save()
        token = _generate_token(JwtUserModel(username))
        return JSONResponse({'token': token, 'id': user.pk, 'username': username})
    except HashingError as err:
        LOGGER.exception(err)
        return Response(status_code=HTTP_401_UNAUTHORIZED)


def login(login: str, password: str) -> Response:
    """Validate password and return dictionary according to result.
    """
    user = _find_user(login)
    if user is None:
        return Response(status_code=HTTP_401_UNAUTHORIZED)
    try:
        pwd_hasher = PasswordHasher()
        if pwd_hasher.verify(user["password"], password):
            # If user was verified, rehash password if it's needed.
            if pwd_hasher.check_needs_rehash(user["password"]):
                _rehash_password(user, password)

            return JSONResponse({
                'id': user.pk,
                'token': _generate_token(JwtUserModel(login)),
                'username': user.username,
            })
        return Response(status_code=HTTP_401_UNAUTHORIZED)

    except (VerificationError, VerifyMismatchError) as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_401_UNAUTHORIZED)
    except InvalidHash as err:
        LOGGER.exception(err)
        return Response(status_code=HTTP_401_UNAUTHORIZED)


def logout(token: str, username: str) -> Response:
    """Logout user with deleting his login token from the database.
    """

    #  TODO remove token from cookie
    token = ''

    return Response(status_code=HTTP_200_OK)
