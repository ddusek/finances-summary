import csv
import json
from mongoengine import connect, NotUniqueError, OperationError, ValidationError
from finances_summary.models.mongo.commodities import Commodities, CommodityType
from finances_summary.settings import MONGO_CONN_URI


def _init_stocks(csv_file: str, skip_header=False) -> tuple[int, int, int]:
    skipped, added, failed = 0, 0, 0
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        if skip_header:
            next(reader)  # Skip header
        print('adding stocks...')
        for row in reader:
            commodity = Commodities(symbol=row[0],
                                    name=row[1],
                                    commodity_type=CommodityType.STOCK.name)
            try:
                commodity.save()
                added += 1
            except NotUniqueError:
                skipped += 1
            except (OperationError, ValidationError):
                failed += 1
        return (skipped, added, failed)


def _init_crypto(json_file: str) -> tuple[int, int, int]:
    skipped, added, failed = 0, 0, 0
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        items = data.items()
        print(f'adding {len(items)} cryptocurrencies...')
        for symbol, name in items:
            commodity = Commodities(symbol=symbol,
                                    name=name,
                                    commodity_type=CommodityType.CRYPTO.name)
            try:
                commodity.save()
                added += 1
            except NotUniqueError:
                skipped += 1
            except (OperationError, ValidationError):
                failed += 1
        return (skipped, added, failed)
