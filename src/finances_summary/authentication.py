from datetime import datetime, timedelta
from jwt import encode, decode
from argon2 import PasswordHasher
from argon2.exceptions import (
    HashingError,
    VerificationError,
    VerifyMismatchError,
    InvalidHash,
)
from bson.objectid import ObjectId
from finances_summary.settings import MONGO, LOGGER, TOKEN_ALGORITHM


# def authorized(func: callable):
#     def decorator(*args, **kwargs):
#         if request.user.is_authenticated:
#             return func
#         else:
#             return Response(status_code=HTTP_401_UNAUTHORIZED)
#     return decorator


def _is_email(login: str) -> bool:
    """Check if login is email or username.
    :param login: login from input.
    :type login: str
    :return: true if email, false if username.
    :rtype: bool
    """
    return "@" in login


def _rehash_password(user, password: str):
    """hash password again if Argon2 parameters change.
    :param user: User Document from mongo.
    :type user: Document
    :param password: Password to rehash.
    :type password: str
    """
    try:
        pwd_hasher = PasswordHasher()
        new_hashed_pwd = pwd_hasher.hash(password)
        MONGO.users.update_one(
            {"username": user.username}, {"$set": {"password": new_hashed_pwd}}
        )
    except HashingError as err:
        LOGGER.exception(err)


def _generate_token(data: dict, expiration: timedelta = timedelta(365)):
    secret_key = "asd"
    expire = datetime.now() + expiration
    data.update({"exp": expire})
    encoded_jwt = encode(data, secret_key, algorithm=TOKEN_ALGORITHM)
    return encoded_jwt


def register_user(username: str, password: str, email: str) -> dict:
    """Register a new user.
    :param username: Username of user.
    :type username: str
    :param password: Password of user.
    :type password: str
    :param email: Email of user.
    :type email: str
    :return: bool about failed/success login, user token and userID if success.
    :rtype: (bool, str)
    """
    if not username:
        raise ValueError("cannot register user, didnt get username")
    if not password:
        raise ValueError("cannot register user, didnt get password")
    if not email:
        raise ValueError("cannot register user, didnt get email")

    exists = MONGO.users.count_documents(
        {"$or": [{"username": username}, {"email": email}]}, limit=1
    )
    if exists > 0:
        return (False, "Username or email already registered.")
    try:
        token = _generate_token({})
        pwd_hasher = PasswordHasher()

        _id = MONGO.users.insert_one(
            {
                "username": username,
                "password": pwd_hasher.hash(password),
                "email": email,
                "created": datetime.now(),
                "last_login": datetime.now(),
                "tokens": [token],
                "collections": {},
            }
        ).inserted_id
        return {"success": True, "token": token, "id": _id, "username": username}
    except HashingError as err:
        LOGGER.exception(err)


def login_user(login: str, password: str) -> dict:
    """Validate password and return dictionary according to result.
    :param login: Username or email of user.
    :type login: str
    :param password: Password of user.
    :type password: str
    :return: {success: bool, user: userID, error: str}.
    :rtype: dict
    """
    user = (
        MONGO.users.find_one({"email": login})
        if _is_email(login)
        else MONGO.users.find_one({"username": login})
    )
    if user is None:
        return {"success": False, "user": 0, "error": "Failed to verify user."}
    try:
        pwd_hasher = PasswordHasher()
        if pwd_hasher.verify(user["password"], password):
            # If user was verified, rehash password if it's needed.
            if pwd_hasher.check_needs_rehash(user["password"]):
                _rehash_password(user, password)

            token = _generate_token(128)
            MONGO.users.update_one(
                {"_id": ObjectId(user["_id"])}, {"$push": {"tokens": token}}
            )
            return {
                "success": True,
                "id": str(user["_id"]),
                "token": token,
                "username": user["username"],
            }
        return {"success": False, "user": 0, "error": "Failed to verify user."}

    except (VerificationError, VerifyMismatchError) as err:
        LOGGER.info(err)
    except InvalidHash as err:
        LOGGER.exception(err)


def logout_user(token: str, user_id: str) -> dict:
    """Logout user with deleting his login token from the database.
    :param token: Username or email of user.
    :type token: str
    :return: {success: bool, user: userID, error: str}.
    :rtype: dict
    """
    user = MONGO.users.update_one(
        {"_id": ObjectId(user_id)}, {"$pull": {"tokens": token}}
    )
    if user.modified_count < 1:
        return {"success": False, "message": "User or token not found."}
    return {"success": True, "message": "token removed from database"}
