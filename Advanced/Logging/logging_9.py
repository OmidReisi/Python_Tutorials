import logging
import Advanced.Logging.logging_6

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r"./Log_Files/logger(logging_9).log")
file_formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler.setFormatter(file_formatter)

# we can specify different levels for our file_handlers as well so only that level and above it gets logged into that file
file_handler.setLevel(logging.ERROR)

# now we add another handler to show our debug messages as well
# we can log messages to our output terminal as well with a StreamHandler
stream_handler = logging.StreamHandler()

# we can also define a format for our stream_handler the same way we did for our file_handler
# the default formatt for StreamHandler is : format = "%(message)s"
stream_handler.setFormatter(file_formatter)

# we should add all our handler's to our logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def multiply(x, y):

    return x * y


def divide(x, y):

    try:
        result = x / y

    except ZeroDivisionError:
        # logger.error("Tried to divide by zero")
        # we can use logging.exception instead of logging.error to get the traceback for the error
        # logging.exception is same as logging.error(message, exc_info=True) but the exception method can only called withing an exception block.
        logger.exception("A ZeroDivisionError occurred")
    else:
        return result


num_1 = 20
num_2 = 0


add_result = add(num_1, num_2)
logger.debug("Add : {} + {} = {}".format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
logger.debug("Add : {} - {} = {}".format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
logger.debug("Add : {} * {} = {}".format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
logger.debug("Add : {} / {} = {}".format(num_1, num_2, div_result))
