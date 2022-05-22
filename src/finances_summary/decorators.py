import functools
import finances_summary


def bind_request(func):
    """Bind current Request to _request variable so it can be accessed
    everywhere without needing to pass request parameter.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        finances_summary.current_request = args[0]
        return await func(*args, **kwargs)
    return wrapper
