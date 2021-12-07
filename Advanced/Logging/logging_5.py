import logging

# to set up a new logger we use the getLogger method
# if the logger already exists then return the logger if not create a new logger
# it is convention to set the module's name (__name__) as logger's name
logger = logging.getLogger(__name__)

# this only sets up our root logger and for setting up our new logger we should set it up differently
# logging in python follows a hierarchy and if we only create are logger and don't set it up then if falls back to root logger configuration and only it's name is equal to our new logger's name
logging.basicConfig(
    filename=r"./Log_Files/employee.log",
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)


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
