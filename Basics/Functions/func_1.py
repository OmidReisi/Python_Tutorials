# use pass to leave a function empty
def empty_func():
    pass


empty_func()

# type function
print(type(empty_func))

# functions with no return value print None
print(empty_func())


def hello_func():
    print("Hello Function")


# greeting is required because does not have a default value
def greet_func(greeting, name="You"):
    return f"{greeting} {name}"


# positional arguments have to come before keyword arguments
print(greet_func(greeting="Hi", name="Omid"))

# *args for positional arguments and **kwargs for keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# args are stored in a tuple and kwargs are stored in a dictionary
student_info("Math", "Art", name="John", age=22)

print()
courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

# unpacks the list and dictionary to be used as args and kwargs respectively
# dicts used as positional arguments only pass their keys
student_info(*courses, **info)
