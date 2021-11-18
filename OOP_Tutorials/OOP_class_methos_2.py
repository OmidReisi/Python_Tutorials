# class methods are used a lot in alternative constructors


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
    # it is convention to use from_ in for alternative constructors
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split("-")
        return cls(first_name, last_name, int(salary))


emp_1 = Employee("Omid", "Reisi", 50000)
emp_2 = Employee("Test", "User", 60000)


emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

emp_3 = Employee.from_string(emp_str_1)
print(emp_3.fullname())

# print(type(emp_3.salary))
# print(type(emp_1.salary))

print(Employee.num_of_emps)
