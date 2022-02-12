# typing is a module in the standard library added to python 3.5
# note that this module allows you to add hints and annotations to your code.
# this module is just for documentation purposes and for example doesn't force you to pass a string to a funcion that is set to type str for it's input.

# static code analysis code is a module that checks if there are mismatches in type annotations(pip install mypy)
# to check if a python script has any mismatches use this command in terminal: mypy <path to your scripts>

# import typing


# this is annoiting that x should store only integers.(but can store other types as well)
x: str = "hey"
print(x)

# this is how type annotations for funcions work
# if a funcion doesn't have any return put None in place of it's return type.
# empty return statement is same as returning None
def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


print(add_numbers(4, 5, 7))
