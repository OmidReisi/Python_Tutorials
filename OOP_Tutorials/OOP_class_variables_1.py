class Employee:

    # this is now a class variable and can only be accessed through the class or it's instances
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        # if we use self.raise_amount it uses instance variable if available
        self.salary = int(self.salary * Employee.raise_amount)


emp_1 = Employee("Omid", "Reisi", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)
print()
print()

# raise_amount is a class variales and emp_1 and emp_2 are using that from their Employee class
# class instances access their attributes in this order:
# 1.their own attributes
# 2. their class attributes
# 3. their inherited class attributes

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print()
print()

# __dict__ method shows the attributes of each one
print(emp_1.__dict__, end="\n\n")
print(emp_2.__dict__, end="\n\n")
print(Employee.__dict__, end="\n\n")

Employee.raise_amount = 1.05

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# when you change a class variable for an instance that variable now becomes an instance variable for that specific instance but remains a class variable as well.
emp_1.raise_amount = 1.10

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)
print(emp_2.__dict__)
