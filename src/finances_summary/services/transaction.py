from decimal import Decimal
from datetime import datetime
from mongoengine.errors import NotUniqueError, OperationError
from starlette.responses import Response
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from finances_summary.models.mongo.user_transactions import TransactionType, UserTransactions
from finances_summary.logger import LOGGER


def add_transaction(date: datetime, record_type: TransactionType, symbol: str,
                    amount: Decimal, price_per_unit: Decimal):
    """Add a new transaction.
    """
    user_transaction = UserTransactions(date=date,
                                        record_type=record_type,
                                        symbol=symbol,
                                        amount=amount,
                                        price_per_unit=price_per_unit)
    try:
        user_transaction.save()
    except (NotUniqueError, OperationError) as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
