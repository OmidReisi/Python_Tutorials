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


class Developer(Employee):
    pass


dev_1 = Developer("Omid", "Reisi", 50000)
dev_2 = Developer("Test", "User", 60000)
emp_1 = Employee("Test2", "User2", 65000)

# prints the number of emps created regardless of their type(e.g. Developer) because this is inherited from Employee class
# print(Developer.num_of_emps)

print(dev_1.email)
print(dev_2.email)

# print(Developer.__dict__)

# print(help(Developer))

#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object
