from mongoengine import Document, StringField, DateField, DecimalField


class CommodityPrices(Document):
    """Commodities historical price data.
    """
    price_date = DateField(required=True)
    symbol = StringField(required=True, unique_with='price_date')
    avg_price = DecimalField(required=True)
    high_price = DecimalField(required=True)
    low_price = DecimalField(required=True)
    volume = DecimalField(required=True)
