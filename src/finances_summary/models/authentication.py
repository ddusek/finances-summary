from datetime import datetime


class JwtUserModel:
    """JWT data of logged in user.
    """
    def __init__(self, username: str):
        self.username: str = username
        self.expiration: datetime
