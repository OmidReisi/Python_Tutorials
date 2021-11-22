def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename=f"Log/decorator_5/{orig_func.__name__}.log", level=logging.INFO
    )

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        orig_func(*args, **kwargs)
        t2 = time.time()
        print(f"{orig_func.__name__} ran in: {t2 - t1} sec")

    return wrapper


@my_logger
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


import time


@my_timer
def display():
    # waits for 1 seconds
    time.sleep(1)
    print("display function")


display_info("Omid", 21)
display()
