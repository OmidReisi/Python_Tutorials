# in order to have multipe decorators on a function you should use this wraps function from functools to preserve the original function in decoration sequences
from functools import wraps


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename=f"Log/decorator_7/{orig_func.__name__}.log", level=logging.INFO
    )
    # this wraps the orig_func and allows decoration sequence
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    # all wrapper functions should be decorated with wraps(orig_func)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        orig_func(*args, **kwargs)
        t2 = time.time()
        print(f"{orig_func.__name__} ran in: {t2 - t1} sec")

    return wrapper


import time


@my_logger
@my_timer
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info("Jack", 30)

# now that this prints display_info we see that by decorating our wrapper function with wraps() function it keep our original function and preserves it's name
print(display_info.__name__)
