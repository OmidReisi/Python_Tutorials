class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


emp_1 = Employee("Omid", "Reisi", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)
print(emp_2.email)

# using a method for displaying fullname is a better option
print("{} {}".format(emp_1.first_name, emp_1.last_name))

print(emp_1.fullname())

# you can run methods with class itself in this case you have to pass the self argument
print(Employee.fullname(emp_2))
