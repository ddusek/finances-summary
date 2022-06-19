import json
from typing import Union
from datetime import datetime


def convert_date(date: str):
    """Convert date from string {mm/dd/yyyy} to datetime object.
    """
    return datetime.strptime(date, '%m/%d/%Y')


def convert_unix_time(date: dict):
    """Convert mongoengine date property to date string in format {mm/dd/yyyy}.
    """
    unix_time = int(str(date['$date'])[:10])
    date_obj = datetime.utcfromtimestamp(unix_time)
    return date_obj.strftime('%m/%d/%Y')


def serialize_json(data: Union[object, list[object]]) -> str:
    if isinstance(data, list):
        return json.dumps([ob.__dict__ for ob in data])
    else:
        return json.dumps(data)
