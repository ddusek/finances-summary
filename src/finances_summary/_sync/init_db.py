from mongoengine import connect
from finances_summary._sync._commodities import _init_crypto, _init_stocks
from finances_summary._sync._historical_data import get_historical_data
from finances_summary.settings import MONGO_CONN_URI

# Connect MongoEngine.
connect(host=MONGO_CONN_URI)

_symbols = ['btc-usd', 'amd', 'crsp', 'crwd', 'bb', 'spce', 'pltr',
            'amc', 'splk', 'goog', 'aapl', 'msft', 'gme', 'coin']


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

    get_historical_data(_symbols)


init_db()
