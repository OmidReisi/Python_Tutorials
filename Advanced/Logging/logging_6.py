import logging


logger = logging.getLogger(__name__)

# the following is how we configure our logger after we've created it:

# first we set our level for our logger
logger.setLevel(logging.INFO)

# then we specify a log_file for our log messages
file_handler = logging.FileHandler(r"./Log_Files/employee_logger(logging_6).log")

# then we create a format for our file handler
file_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

# then we add our formatter to our file_handler
# it is very important to know that we add our formatter to our file and not our logger
file_handler.setFormatter(file_formatter)

# finally we add our log_file as a file_handler
logger.addHandler(file_handler)


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # when we set up a new logger we should use our logger variable to run the log messages
        logger.info("Created Employee {} - {}".format(self.full_name, self.email))

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Omid", "Reisi")
emp_3 = Employee("Jane", "Doe")
