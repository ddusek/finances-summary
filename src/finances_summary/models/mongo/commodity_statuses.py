from mongoengine import Document, StringField, BooleanField


class CommodityStatuses(Document):
    """Commodities historical price data.
    """
    symbol = StringField(required=True)
    imported = BooleanField(required=True)
