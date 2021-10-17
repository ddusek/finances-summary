from datetime import datetime


def convert_date(date: str):
    """Convert date from string {mm/dd/yyyy} to datetime object.
    """
    return datetime.strptime(date, '%m/%d/%Y')
