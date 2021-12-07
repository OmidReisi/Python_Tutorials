import logging

# now that we have set up a different logger in our imported module then when we import it it uses it's own log configuration and log_file
import Advanced.Logging.logging_6


# this current running module doesn't have it's own logger so it uses the root logger's configuration
logging.basicConfig(
    filename=r"./Log_Files/rootlogger(logger_7).log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


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
logging.debug("Add : {} + {} = {}".format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
logging.debug("Add : {} - {} = {}".format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
logging.debug("Add : {} * {} = {}".format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
logging.debug("Add : {} / {} = {}".format(num_1, num_2, div_result))
