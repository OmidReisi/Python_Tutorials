# Python Object-Oriented Programming


class Employee:
    pass


# this is an instance of a class
emp_1 = Employee()
emp_2 = Employee()


print(type(emp_1))
print(type(Employee))

print()
print()

emp_1.first_name = "Omid"
emp_1.last_name = "Reisi"
emp_1.email_address = "Omid.Reisi@company.com"
emp_1.salary = 50000

emp_2.first_name = "Test"
emp_2.last_name = "User"
emp_2.email_address = "Test.User@company.com"
emp_2.salary = 60000

print(emp_1.email_address)
print(emp_2.email_address)
