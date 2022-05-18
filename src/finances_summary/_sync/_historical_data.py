import yfinance as yf
from finances_summary.models.mongo.commodity_prices import CommodityPrices
from finances_summary.models.mongo.commodity_statuses import CommodityStatuses
from mongoengine.errors import NotUniqueError, OperationError, ValidationError
from pandas import DataFrame


def _add_symbol_data(symbol: str) -> tuple[int, int, int]:
    ticker = yf.Ticker(symbol)
    data: DataFrame = ticker.history(period='max')
    skipped, added, failed = 0, 0, 0
    for i, r in data.iterrows():
        status = CommodityStatuses.objects(symbol=symbol).first()
        if (not status or not status.imported):
            record = CommodityPrices(price_date=i.to_pydatetime(),
                                     symbol=symbol,
                                     high_price=r['High'],
                                     low_price=r['Low'],
                                     avg_price=(r['High'] + r["Low"]) / 2,
                                     volume=r['Volume'])
            try:
                record.save()
                added += 1
            except NotUniqueError:
                skipped += 1
            except (OperationError, ValidationError):
                failed += 1
    return (skipped, added, failed)


def get_historical_data(symbols: list[str]):
    results: dict[str, tuple[int, int, int]] = {}
    for symbol in symbols:
        symbolStatus = CommodityStatuses.objects(symbol=symbol).first()
        if (symbolStatus is None or symbolStatus.imported is not True):
            print(f'adding {symbol}...')
            res = _add_symbol_data(symbol)
            results[symbol] = res
            symbolStatus = CommodityStatuses(symbol=symbol, imported=True)
            symbolStatus.save()

    # print results
    for k, v in results.items():
        print(f'{k}: added: {v[1]} skipped: {v[0]} failed: {v[2]}')
