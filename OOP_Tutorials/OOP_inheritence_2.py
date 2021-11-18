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


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):

        # calls the inherited class __init__ method
        super().__init__(first_name, last_name, salary)

        # this works like above and is essential for multi-inheritence but for single-inheritence super().__init__ is recommended
        # Employee.__init__(self, first_name, last_name, salary)

        self.prog_lang = prog_lang

    def info(self):

        # this is a good example for dictionary unpacking
        return {**super().info(), "prog_lang": self.prog_lang}

        # remember dict.update does not return any value so in this alternative you need all the three lines below
        # info = super().info()
        # info.update({"Prog_lang": self.prog_lang})
        # return info


dev_1 = Developer("Omid", "Reisi", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")
emp_1 = Employee("Test2", "User2", 50000)

print(dev_1.salary)
dev_1.apply_raise()
print(dev_1.salary)

print()
print()

print(emp_1.info())

print()
print()

print(dev_1.info())
