import functools
from finances_summary import variables


def bind_request(func):
    """Bind current Request to _request variable so it can be accessed
    everywhere without needing to pass request parameter everywhere.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        variables.request_ = args[0]
        return await func(*args, **kwargs)
    return wrapper
