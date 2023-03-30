import time
from functools import wraps
from loguru import logger



# retry decorator
def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    logger.info(f"Try #{tries+1} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        logger.error(f"Failed to execute {func.__name__}")
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry

# cache decorator
def memoize(func):
    cache = dict()
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

# running time decorator
def timeit(func, precision=3):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Running time for {func.__name__}: {round(end_time-start_time, precision)} seconds")
        return result
    return wrapper


# logging execution decorator
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished executing: {func.__name__}")
        return result
    return wrapper


