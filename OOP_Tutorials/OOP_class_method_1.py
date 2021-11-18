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

    # you create class methods by using classmethod decorator on top of the method
    # class methods take the class itself(cls) as their first argument insetead of the instance(self)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee("Omid", "Reisi", 50000)
emp_2 = Employee("Test", "User", 60000)

Employee.set_raise_amount(1.05)

# you can run class methods with instances as well which works the same but it is not recommended
# emp_1.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(Employee.__dict__)
