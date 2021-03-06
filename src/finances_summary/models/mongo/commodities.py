from finances_summary.models.enums import CommodityType
from enum import Enum
from mongoengine import Document, StringField


class Commodities(Document):
    """All commodities symbols and names.
    """
    symbol = StringField(required=True)
    name = StringField(required=True)
    commodity_type = StringField(choices=[
        CommodityType.STOCK.name, CommodityType.CRYPTO.name
    ],
                                 required=True,
                                 unique_with='symbol')
