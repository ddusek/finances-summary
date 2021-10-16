from finances_summary.services.authentication import decode_token
from finances_summary.variables import request_


def get_user_token() -> str:
    if request_:
        cookies = request_.cookies
        return cookies['token'] if 'token' in cookies else ''
    return ''


def get_current_user_id() -> str:
    token = get_user_token()
    if token:
        data = decode_token(token)
        if data:
            return str(data.user_id)
    return ''
