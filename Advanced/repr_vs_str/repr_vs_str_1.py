# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable

# __repr__ is used for debuging and logging and usually shows something that can be used as a python command and is meant for developers eyes
# __str__ is just a string representation of an object and is user friendly

a = [1, 2, 3, 4]
b = "sample string"

print(str(a))
print(repr(a))

print()
print()

print(str(b))
print(repr(b))
