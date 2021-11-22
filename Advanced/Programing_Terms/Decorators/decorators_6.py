def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename=f"Log/decorator_6/{orig_func.__name__}.log", level=logging.INFO
    )

    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        print("this is wrapper function in my_logger")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        orig_func(*args, **kwargs)
        t2 = time.time()
        print(f"{orig_func.__name__} ran in: {t2 - t1} sec")
        print("this is wrapper function in my_timer")

    return wrapper


import time

# # this is same as saying display_info = my_timer(my_logger(display_info))
# # this one runs the timer on my_logger's wrapper function
# @my_timer
# @my_logger
# def display_info(name, age):
#     print("display_info ran with arguments ({}, {})".format(name, age))


# # this is same as saying display_info = my_logger(my_timer(display_info))
# # this one creates a wrapper.log file
# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("display_info ran with arguments ({}, {})".format(name, age))


# non of the above works correctly because the outer decorator runs on the other decorator wrapper function not the original function itself
# display_info("John", 25)


# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("display_info ran with arguments ({}, {})".format(name, age))


# display_info("John", 25)

# # this prints wrapper because decorators return wrapper function and display_info is no longer the name of this function
# print(display_info.__name__)
