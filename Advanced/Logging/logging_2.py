# The following are the different logging levels:


# DEBUG(10): Detailed information, typically of interest only when diagnosing problems.

# INFO(20): Confirmation that things are working as expected.

# WARNING(30): An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR(40): Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL(50): A serious error, indicating that the program itself may be unable to continue running.

# the different logging levels are in order and the default level is debug which means logging catches everythig the is a debug or ABOVE (ERROR and CRITICAL)


import logging


# logging.basicConfig method allows us to configure our logging optionos
# remember that logging levels are all caps and their methods are all lowercase
# if we don't want to log to the output terminal and we want to use a log file we specify it here
# we can change the logging format with the format keyword
# the default logging format is : format = "%(levelname)s:%(name)s:%(message)s"
# different formats are available below
# https://python.readthedocs.io/en/latest/library/logging.html#logrecord-attributes

logging.basicConfig(
    filename=r"./Log_Files/log_1.log",
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
