from enum import Enum
from mongoengine import Document, StringField, DateTimeField, ObjectIdField, DecimalField


class TransactionType(Enum):
    """Type of record.
    """
    BUY = 1
    SELL = 2


class UserTransactions(Document):
    """All user records (buys, sells, etc...).
    """
    user = ObjectIdField(required=True)
    date = DateTimeField(required=True)
    record_type = StringField(choices=[
        TransactionType.BUY.name, TransactionType.SELL.name
    ],
                              required=True)
    symbol = StringField(required=True)
    amount = DecimalField(precision=9, required=True)
    price_per_unit = DecimalField(precision=9, required=True)
    fee = DecimalField()
