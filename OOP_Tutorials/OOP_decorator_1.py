class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # because python has a garbage collector at the end of every program every object gets destructed so this method runs
    def __del__(self):
        print("Object was deleted!")

    # this property decorator( @property) makes methods to act like attributes
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # this setter decorator allows us to change the value of our property
    # use the {propety name}.setter in this example fullname.setter decorator followed by a method with the same name as your property
    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first_name = None
        self.last_name = None


emp_1 = Employee("John", "Smith")

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first_name = "Jim"

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)


emp_1.fullname = "Omid Reisi"

print(emp_1.first_name)
print(emp_1.email)

del emp_1.fullname
