import functools
import logging

logger = logging.getLogger(__name__)


def log_exceptions(func):
    """
    Decorator that catches exceptions and logs them.

    :param func: The function to be decorated.
    :return: The decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.exception(f"Exception occurred in {func.__name__}: {error}")
            raise

    return wrapper
