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

    # print statements and calling __str__ method use __repr__ if __str__ is not implemented
    def __repr__(self):
        return "repr"

    # by default print statements use __str__
    def __str__(self):
        return "str"


# if __str__ or __repr__ is used for print function then they must return a string


emp_1 = Employee("Omid", "Reisi", 60000)
print(emp_1)

# also emp_1.__repr__()
print(repr(emp_1))

# also emp1.__str__()
print(str(emp_1))
