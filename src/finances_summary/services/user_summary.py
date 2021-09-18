from decimal import Decimal
from datetime import datetime
from bson import ObjectId
from mongoengine.errors import NotUniqueError, OperationError, ValidationError
from starlette.responses import Response, JSONResponse
from starlette.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
                              HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_500_INTERNAL_SERVER_ERROR)
from finances_summary.models.mongo.user_transactions import (
    TransactionType,
    UserTransactions,
)
from finances_summary.logger import LOGGER


def total() -> Response:
    raise NotImplementedError()


def symbol(symbol_name: str) -> Response:
    raise NotImplementedError()
