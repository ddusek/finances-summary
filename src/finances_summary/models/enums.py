from enum import Enum


class TransactionType(Enum):
    """Type of record.
    """
    BUY = 1
    SELL = 2


class CommodityType(Enum):
    """Type of record.
    """
    STOCK = 1
    CRYPTO = 2
