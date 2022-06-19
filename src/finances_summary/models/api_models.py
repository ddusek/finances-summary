from decimal import Decimal
from dataclasses import dataclass
from finances_summary.models.base import BaseResponse
from finances_summary.models.enums import TransactionType


@dataclass
class JwtUserModel:
    """JWT data of logged in user.
    """
    username: str
    user_id: str
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


@dataclass
class Transaction():
    date: str
    record_type: TransactionType
    symbol: str
    amount: Decimal
    price_per_unit: Decimal
    fee: Decimal
