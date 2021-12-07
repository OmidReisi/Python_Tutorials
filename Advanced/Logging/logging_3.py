import logging

logging.basicConfig(
    filename=r"./Log_Files/employee.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
)


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        logging.info("Created Employee {} - {}".format(self.full_name, self.email))

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Omid", "Reisi")
emp_3 = Employee("Jane", "Doe")
