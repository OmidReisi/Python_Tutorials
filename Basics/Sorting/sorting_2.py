# attrgetter returns a callable object that refers to that attribute
from operator import attrgetter


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name}, {self.age}, ${self.salary})"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

emps = [e1, e2, e3]

# python does not know how to sort instance of a class so you have to use key parameter
# s_emps = sorted(emps)
# print(s_emps)


# def e_sort(emp):
#     return emp.name

# s_emps = sorted(emps, key=e_sort)
# print(s_emps)


# s_emps = sorted(emps, key=lambda emp: emp.name)
# print(s_emps)

# name now refer to any object that has an attribute called name
name = attrgetter("name")
print(name(e1))

s_emps = sorted(emps, key=attrgetter("name"))
print(s_emps)
