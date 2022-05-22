from bson import ObjectId
from finances_summary.services.jwt_service import decode_token
from finances_summary.services.cookies import get_user_token


def get_current_user_id(as_string=True) -> str:
    token = get_user_token()
    if token:
        data = decode_token(token)
        if data:
            print(data)
            if as_string:
                return data.user_id
            return ObjectId(data.user_id)
    return ''
