"""
LEGB
Local, Enclosing, Global, Built-in
this is order which variables are assigned to
"""
# Locals are variable defined in a function
# Enclosing are variables in the local scope of enclosing function (outer function)
# Global are variables defined at the top level module or explicitly defined with global keyword
# Built-in are names pre-assinged in python


# this is a global variable because it is in the main body of our module
x = "global x"


def test_1():
    # this is a local variable and only accessable through the body of test function
    y = "local y"
    print(y)
    # there is no local and enclosing x so it falls back to global x variable
    print(x)


test_1()

# there is no global or built-in variable named y so we get an error
# print(y)


def test_2():
    x = "local x"
    # now that there is a local x variable and local varialbes are used first this prints local x
    print(x)


test_2()

# here we don't have access to x varialbe in test_2 function so this uses global x variable
print(x)


def test_3():
    # this line here explicitly says that we want to use global x variable and now changes the value of our global x variable set before
    global x
    x = "global x used in test_3 function"
    print(x)


test_3()
# test_3 function changed the value of our global x so these 2 lines here print the same thing and ore refering to the same object
print(x)


def test_4():
    global y
    y = "global y variable used in test_4 function"
    print(y)


# this is same as test_3 function but we don't have to have a y variable defined before, in order to use it in our function basiclly global y line sees that if a global y exists then refers to that if not creates a new global variable y
test_4()
print(y)

# z is now same as a variable defined in test_5 function and is considered a local varialbe to test_5 function
def test_5(z):
    print(z)


test_5("local z")
