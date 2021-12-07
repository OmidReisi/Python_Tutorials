import logging
import Advanced.Logging.logging_6

# now we set up a new logger for our main module as well
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r"./Log_Files/logger(logging_8).log")
file_formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def multiply(x, y):

    return x * y


def divide(x, y):

    return x / y


num_1 = 20
num_2 = 10


add_result = add(num_1, num_2)
logger.debug("Add : {} + {} = {}".format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
logger.debug("Add : {} - {} = {}".format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
logger.debug("Add : {} * {} = {}".format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
logger.debug("Add : {} / {} = {}".format(num_1, num_2, div_result))
