from starlette.responses import Response
import finances_summary


def get_cookie(token: str) -> str:
    cookies = finances_summary.current_request.cookies
    return cookies['token'] if 'token' in cookies else ''


def get_user_token() -> str:
    return get_cookie('token')


def set_cookie(response: Response,
               key: str,
               value: str,
               expires=60 * 60 * 24 * 365,
               samesite='none',
               secure=True):
    response.set_cookie(key, value, expires=expires, samesite=samesite, secure=secure)
