from bson import ObjectId
from finances_summary.services.authentication import decode_token
import finances_summary


def get_user_token() -> str:
    print(finances_summary.request_)
    if finances_summary.request_:
        cookies = finances_summary.request_.cookies
        return cookies['token'] if 'token' in cookies else ''
    return ''


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
