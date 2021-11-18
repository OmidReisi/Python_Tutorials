# static methods don't pass class instance (self) or class itself (cls) automatically and they're just like regular functions except they have some logical connection to the class and that is why we include them in the class


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split("-")
        return cls(first_name, last_name, int(salary))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("Omid", "Reisi", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime

my_date = datetime.date(2021, 11, 18)

# print(my_date.weekday())

print(Employee.is_workday(my_date))
