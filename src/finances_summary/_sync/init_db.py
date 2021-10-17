import csv
import json
from mongoengine import connect, NotUniqueError, OperationError, ValidationError
from finances_summary.models.mongo.commodities import Commodities, CommodityType
from finances_summary.settings import MONGO_CONN_URI

# Connect MongoEngine.
connect(host=MONGO_CONN_URI)


def _init_stocks(csv_file: str, skip_header=False) -> tuple[int, int, int]:
    skipped, added, failed = 0, 0, 0
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        if skip_header:
            next(reader)  # Skip header
        print(f'adding stocks...')
        for row in reader:
            commodity = Commodities(symbol=row[0],
                                    name=row[1],
                                    commodity_type=CommodityType.STOCK.name)
            try:
                commodity.save()
                added += 1
                # print(f'added stock {row[0]} - {row[1]}')
            except NotUniqueError:
                skipped += 1
                # print(f'skipped stock {row[0]} - {row[1]}')
            except (OperationError, ValidationError):
                failed += 1
                # print(f'failed stock {row[0]} - {row[1]}\nerr: {e}')
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
                # print(f'added crypto {symbol} - {name}')
            except NotUniqueError:
                skipped += 1
                # print(f'skipped crypto {symbol} - {name}')
            except (OperationError, ValidationError) as e:
                failed += 1
                # print(f'failed crypto {symbol} - {name}\nerr: {e}')
        return (skipped, added, failed)


def init_db() -> None:
    """Init database data.
    """
    stocks_result = _init_stocks('finances_summary/_sync/data/symbols-stocks.csv', True)
    crypto_result = _init_crypto('finances_summary/_sync/data/symbols-crypto.json')
    print(f'''\nstocks:
    skipped {stocks_result[0]}
    added {stocks_result[1]}
    failed {stocks_result[2]}
crypto:
    skipped {crypto_result[0]}
    added {crypto_result[1]}
    failed {crypto_result[2]}''')


init_db()
