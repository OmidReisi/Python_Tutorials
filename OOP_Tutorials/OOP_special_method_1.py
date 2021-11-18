# special methods (or magic methods) (or dunder methods) are methods that start and end with "__"


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

    def info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "salary": self.salary,
            "email": self.email,
        }

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    def __repr__(self):
        return f"instance of class Employee: Employee({self.first_name}, {self.last_name}, {self.salary})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"


emp_1 = Employee("Omid", "Reisi", 60000)

print(repr(emp_1))
print(str(emp_1))
print(emp_1)
