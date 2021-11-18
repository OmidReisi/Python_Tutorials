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
    num_of_emps = 0

    def __init__(self, first_name, last_name, salary, prog_lang):

        super().__init__(first_name, last_name, salary)

        self.prog_lang = prog_lang
        Developer.num_of_emps += 1

    def info(self):

        return {**super().info(), "prog_lang": self.prog_lang}


class Manager(Employee):

    num_of_emps = 0

    # emps shows the list of employees that a manager controls
    # it is NOT recommended to pass empty mutables such as list as default of an argument
    def __init__(self, first_name, last_name, salary, emps=None):
        super().__init__(first_name, last_name, salary)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

        Manager.num_of_emps += 1

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def show_emps(self):
        for emp in self.emps:
            print("-->", emp.info())


dev_1 = Developer("Omid", "Reisi", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.info())
print()

mgr_1.show_emps()
print()
print()

mgr_1.add_emp(dev_2)

mgr_1.show_emps()
print()
print()

mgr_1.remove_emp(dev_1)

mgr_1.show_emps()
print()
print()

print("number of employees:", Employee.num_of_emps)
print("number of Developers:", Developer.num_of_emps)
print("number of Managers:", Manager.num_of_emps)

print()
print()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print()
print()

# a class is always a subclass of itself regradless of inheritence
print(issubclass(Manager, Manager))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))
