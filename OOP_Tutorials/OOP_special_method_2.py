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

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        else:
            # returning NotImplemented is a way to see if the other object knows how to handle this situation without throwing an error
            return NotImplemented

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Omid", "Reisi", 60000)
emp_2 = Employee("Test", "User", 40000)


print(int.__add__(2, 3))
print(str.__add__("a", "b"))

print(emp_1 + emp_2)

# len() is another special method
print(str.__len__("test"))

print(len(emp_1))


# special-method-names
# https://docs.python.org/3/reference/datamodel.html
