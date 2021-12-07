import logging
import logging_3

# when we import loggin_3 because it has already set up the logging configuration and we are using the root logger and not creating a different logger then that configuration does not change here and it doesn't create the new log file
# the following doesn't log anything because we have setup the logging level to INFO in the imported module
logging.basicConfig(
    filename=r"./Log_Files/root(logging_4).log",
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

# if we change the logging messages to info then these messages will also log in employee.log

add_result = add(num_1, num_2)
logging.info("Add : {} + {} = {}".format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)
logging.info("Add : {} - {} = {}".format(num_1, num_2, sub_result))


mul_result = multiply(num_1, num_2)
logging.info("Add : {} * {} = {}".format(num_1, num_2, mul_result))


div_result = divide(num_1, num_2)
logging.info("Add : {} / {} = {}".format(num_1, num_2, div_result))
