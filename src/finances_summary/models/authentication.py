from dataclasses import dataclass
from finances_summary.models.base import BaseResponse


@dataclass
class JwtUserModel:
    """JWT data of logged in user.
    """
    username: str
    expiration: str = ''


@dataclass
class RegistrationConflict:
    """Conflict fields on registration.
    """
    username_conflict: bool = False
    email_conflict: bool = False


@dataclass
class RegistrationResponse(BaseResponse):
    """Response on registration.
    """
    success: bool = True
    username_conflict: bool = False
    email_conflict: bool = False
    token: str = ''
    _id: str = ''
    username: str = ''


@dataclass
class AuthorizedResponse(BaseResponse):
    """Response on authorized request.
    """
    authorized: bool = False
