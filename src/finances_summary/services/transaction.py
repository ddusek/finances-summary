from decimal import Decimal
from datetime import datetime
from bson import ObjectId
from mongoengine.errors import OperationError, ValidationError
from starlette.responses import Response, JSONResponse
from starlette.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
                              HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_500_INTERNAL_SERVER_ERROR)
from finances_summary.logger import LOGGER
from finances_summary.models.mongo.user_transactions import (
    TransactionType,
    UserTransactions,
)
from finances_summary.services.user import get_current_user_id


def add(date: datetime, record_type: TransactionType, symbol: str, amount: Decimal,
        fee: Decimal, price_per_unit: Decimal) -> Response:
    """Add a new transaction.
    """
    user_transaction = UserTransactions(
        user=get_current_user_id(),
        date=date,
        record_type=record_type,
        symbol=symbol,
        amount=amount,
        price_per_unit=price_per_unit,
    )
    try:
        user_transaction.save()
        return Response(status_code=HTTP_201_CREATED)
    except OperationError as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except (ValidationError) as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_422_UNPROCESSABLE_ENTITY)


def remove(object_id: ObjectId) -> Response:
    """Remove a transaction.
    """
    transaction = UserTransactions.objects(ObjectId=object_id).first()
    if transaction is not None:
        try:
            transaction.delete()
            return Response(status_code=HTTP_200_OK)
        except OperationError:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    LOGGER.error('tried to delete a non-existing transaction %s', object_id)
    return Response(status_code=HTTP_404_NOT_FOUND)


def list_(type_: str = None, symbol: str = None) -> Response:
    """Get list of user's transactions.
    """
    # TODO check if query can be built with multiple calls
    # of 'objects()' without multiple db calls.
    # TODO add userID from jwt token to query.
    query = {}
    if type_ is not None:
        try:
            query['type'] = TransactionType[type_]
        except KeyError:
            return Response(status_code=HTTP_400_BAD_REQUEST)
    if symbol is not None:
        query['symbol'] = symbol
    # TODO pagination.
    transactions = UserTransactions.objects(__raw__=query)[:50]
    return JSONResponse(transactions)
