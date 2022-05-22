from jwt import decode, DecodeError
from argon2 import PasswordHasher
from argon2.exceptions import (HashingError, VerificationError, VerifyMismatchError,
                               InvalidHash)
from mongoengine import ValidationError, Q
from starlette.responses import JSONResponse, Response
from starlette.status import (HTTP_401_UNAUTHORIZED, HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_409_CONFLICT)
from finances_summary.logger import LOGGER
from finances_summary.models.authentication import (
    JwtUserModel, RegistrationConflict, RegistrationResponse, AuthorizedResponse)
from finances_summary.models.mongo.users import Users
from finances_summary.settings import (JWT_ALGORITHM, JWT_PUBLIC_KEY_PATH)
from finances_summary.services.jwt_service import generate_token, is_token_valid
from finances_summary.services.cookies import set_cookie


def _is_email(login: str) -> bool:
    """Check if login is email or username.
    """
    return "@" in login


def _rehash_password(user: Users, password: str) -> None:
    """hash password again if Argon2 parameters change.
    """
    try:
        pwd_hasher = PasswordHasher()
        new_hashed_pwd = pwd_hasher.hash(password)
        user.password = new_hashed_pwd
        user.update()

    except HashingError as err:
        LOGGER.exception(err)


def _find_user(login: str) -> Users:
    """Find user either by email or username.
    """
    if _is_email(login):
        return Users.objects(email=login).first()
    return Users.objects(username=login).first()


def _has_conflicts(username: str, email: str) -> RegistrationConflict:
    """Check if username and/or email is already used.
    Return Tuple of booleans (username_used, email_used).
    """
    users = Users.objects(Q(username=username) | Q(email=email))
    conflict = RegistrationConflict()
    for user in users:
        if user.username == username:
            conflict.username_conflict = True
        if user.email == email:
            conflict.email_conflict = True
    return conflict


def register(username: str, password: str, email: str) -> Response:
    """Register a new user.
    """
    if not username or not password or not email:
        return Response(status_code=HTTP_422_UNPROCESSABLE_ENTITY)

    conflicts = _has_conflicts(username, email)
    if conflicts.username_conflict or conflicts.email_conflict:
        # Username and/or email already exist.
        reg_response = RegistrationResponse(False, conflicts.username_conflict,
                                            conflicts.email_conflict)
        return JSONResponse(reg_response.as_dict(), status_code=HTTP_409_CONFLICT)
    try:
        pwd_hasher = PasswordHasher()
        hashed_pwd = pwd_hasher.hash(password)
        user = Users().create_new(username, email, hashed_pwd)
        user.save()
        jwt_user = JwtUserModel(username, str(user.id))
        token = generate_token(jwt_user)
        # Success response.
        reg_response = RegistrationResponse(token=token,
                                            _id=str(user.id),
                                            username=username)
        response = JSONResponse(reg_response.as_dict())
        response.set_cookie('token',
                            token,
                            expires=60 * 60 * 24 * 365,
                            httponly=True,
                            secure=True)
        return response
    except (HashingError, ValidationError) as err:
        LOGGER.exception(err)
        return Response(status_code=HTTP_422_UNPROCESSABLE_ENTITY)


def login(login: str, password: str) -> Response:
    """Validate password and set token cookie.
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
            response = JSONResponse({
                'id': str(user.id),
                'username': user.username,
            })
            token = generate_token(JwtUserModel(login, str(user.id)))
            set_cookie(response, 'token', token)

            return response
        return Response(status_code=HTTP_401_UNAUTHORIZED)

    except (VerificationError, VerifyMismatchError) as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_401_UNAUTHORIZED)
    except InvalidHash as err:
        LOGGER.exception(err)
        return Response(status_code=HTTP_401_UNAUTHORIZED)


def is_user_authenticated(token: str) -> Response:
    """Verify user token.
    """
    if is_token_valid(token):
        return JSONResponse(AuthorizedResponse(True).as_dict())
    return JSONResponse(AuthorizedResponse().as_dict())
