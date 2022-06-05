from bson import ObjectId
from finances_summary.services.jwt_service import decode_token
from finances_summary.services.cookies import get_user_token


def user_objectId() -> ObjectId:
    token = get_user_token()
    if token:
        data = decode_token(token)
        if data:
            print(data)
            return ObjectId(data.user_id)
    return ''
