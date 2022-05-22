from typing import Union
from datetime import datetime, timedelta
from jwt import encode, decode, DecodeError
from finances_summary.models.authentication import JwtUserModel
from finances_summary.settings import (JWT_ALGORITHM, JWT_PRIVATE_KEY_PATH,
                                       JWT_PUBLIC_KEY_PATH)


def generate_token(data: JwtUserModel, expiration: timedelta = timedelta(365)) -> str:
    """Generate JWT token.
    """
    expire = datetime.now() + expiration
    data.expiration = expire.isoformat()
    with open(JWT_PRIVATE_KEY_PATH, 'r', encoding='UTF-8') as file:
        encoded_jwt = encode(data.__dict__, key=file.read(), algorithm=JWT_ALGORITHM)
        return encoded_jwt


def decode_token(token: str) -> Union[JwtUserModel, None]:
    if not token:
        return None
    with open(JWT_PUBLIC_KEY_PATH, 'r', encoding='UTF-8') as file:
        try:
            json_data = decode(token, file.read(), algorithms=[JWT_ALGORITHM])
            return JwtUserModel(**json_data)
        except DecodeError:
            return None


def is_token_valid(token: str) -> bool:
    """Return True if jwt token is valid.
    """
    if not token:
        return False
    with open(JWT_PUBLIC_KEY_PATH, 'r', encoding='UTF-8') as file:
        try:
            decode(token, file.read(), algorithms=[JWT_ALGORITHM])
            return True
        except DecodeError:
            return False
