from datetime import datetime, timedelta
from jwt import encode
from argon2 import PasswordHasher
from argon2.exceptions import (HashingError, VerificationError, VerifyMismatchError,
                               InvalidHash)
from mongoengine import ValidationError, Q
from starlette.responses import JSONResponse, Response
from starlette.status import (HTTP_401_UNAUTHORIZED, HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_409_CONFLICT, HTTP_200_OK)
from finances_summary.logger import LOGGER
from finances_summary.models.authentication import (JwtUserModel, RegistrationConflict,
                                                    RegistrationResponse)
from finances_summary.models.mongo.users import Users
from finances_summary.settings import (JWT_ALGORITHM, JWT_PRIVATE_KEY_PATH,
                                       JWT_PUBLIC_KEY_PATH)

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


def _generate_token(data: JwtUserModel, expiration: timedelta = timedelta(365)) -> str:
    """Generate JWT token.
    """
    expire = datetime.now() + expiration
    data.expiration = expire.isoformat()
    with open(JWT_PRIVATE_KEY_PATH, 'r', encoding='UTF-8') as file:
        encoded_jwt = encode(data.__dict__, key=file.read(), algorithm=JWT_ALGORITHM)
        return encoded_jwt


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
        response = RegistrationResponse(False, conflicts.username_conflict,
                                        conflicts.email_conflict)
        return JSONResponse(response.as_dict(), status_code=HTTP_409_CONFLICT)
    try:
        token = _generate_token(JwtUserModel(username))
        pwd_hasher = PasswordHasher()
        user = Users().create_new(username, email, pwd_hasher.hash(password))
        user.save()
        # Success response.
        response = RegistrationResponse(token=token, _id=str(user.pk), username=username)
        return JSONResponse(response.as_dict())
    except (HashingError, ValidationError) as err:
        LOGGER.exception(err)
        return Response(status_code=HTTP_422_UNPROCESSABLE_ENTITY)


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
                'id': str(user.pk),
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
    """Logout user.
    """

    #  TODO remove token from cookie, endpoint might not be needed.
    token = ''

    return Response(status_code=HTTP_200_OK)
