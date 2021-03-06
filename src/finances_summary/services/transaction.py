import json
from decimal import Decimal
from bson import ObjectId
from mongoengine.errors import OperationError, ValidationError
from starlette.responses import Response
from starlette.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
                              HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_500_INTERNAL_SERVER_ERROR)
from finances_summary.logger import LOGGER
from finances_summary.converters import convert_date, convert_unix_time, serialize_json
from finances_summary.models.mongo.user_transactions import (
    TransactionType, UserTransactions, Transaction)
from finances_summary.models.api_models import (JwtUserModel, Transaction as
                                                TransactionResponse)
from finances_summary.services.user import user_objectId


def add(date: str, record_type: TransactionType, symbol: str, amount: Decimal,
        fee: Decimal, price_per_unit: Decimal) -> Response:
    """Add a new transaction.
    """
    transaction = Transaction(
        date=convert_date(date),
        record_type=record_type,
        symbol=symbol,
        amount=amount,
        price_per_unit=price_per_unit,
        fee=fee,
    )
    user_transactions = UserTransactions.objects(user=user_objectId())
    try:
        if (user_transactions):
            user_transactions.update_one(push__transactions=transaction)
        else:
            user_transaction = UserTransactions(user=user_objectId(),
                                                transactions=[transaction])
            user_transaction.save()
        return Response(status_code=HTTP_201_CREATED)
    except OperationError as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except (ValidationError) as err:
        LOGGER.info(err)
        return Response(status_code=HTTP_422_UNPROCESSABLE_ENTITY)


def remove(_id: ObjectId) -> Response:
    """Remove a transaction.
    """
    transaction = UserTransactions.objects(ObjectId=_id).first()
    if transaction is not None:
        try:
            transaction.delete()
            return Response(status_code=HTTP_200_OK)
        except OperationError:
            return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    LOGGER.error('tried to delete a non-existing transaction %s', _id)
    return Response(status_code=HTTP_404_NOT_FOUND)


def list_(user: JwtUserModel, type_: str = None, symbol: str = None) -> Response:
    """Get list of user's transactions.
    """
    # TODO filter by transaction type and symbols
    query = {}
    if type_ is not None:
        try:
            pass
            # query['record_type'] = TransactionType[type_].name
        except KeyError:
            return Response(status_code=HTTP_400_BAD_REQUEST)
    if symbol is not None:
        pass
        # query['symbol'] = symbol
    if user is not None:
        query['user'] = ObjectId(user.user_id)
    # TODO pagination.
    user_transactions = UserTransactions.objects(**query).first()
    transactions = json.loads(user_transactions.to_json())
    print(transactions)
    transactions_response = [
        TransactionResponse(date=convert_unix_time(t['date']),
                            record_type=t['record_type'],
                            symbol=t['symbol'],
                            amount=t['amount'],
                            price_per_unit=t['price_per_unit'],
                            fee=t['fee']) for t in transactions['transactions']
    ]
    print(transactions_response)
    return Response(serialize_json(transactions_response))
