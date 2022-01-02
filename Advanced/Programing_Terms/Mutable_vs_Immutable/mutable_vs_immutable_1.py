# MUTABLE: An object that it's state can be changed after it's created
# IMMUTABLE: An object that it's state can NOT be changed after it's created


# in python string are considered IMMUTABLE this means that every time you change the value of a string variable you're creating a new object

s1 = "string object 1"
print(f"{s1}: {id(s1)}")

# notice that when we pass a new string the object id changes and creaats a new object (you have to change the string if you pass the same string the object does not change)
s1 = "string object 2"
print(f"{s1}: {id(s1)}")

# because strings are immutable they don't support item assignment and you cant' change a single character's value (following code raises an error)
# s1[0] = "S"


# lists in python are MUTABLE

a = [1, 2, 3, 4, 5]
print(f"{a}: {id(a)}")

# when ever you assing a new value to your variable object it creates a new object in memory and it doesn't matter if your object is mutable or immutable
# for lists if you even pass the same value as before it still changes the id and creates a new object
a = [1, 2, 3, 4, 5]
print(f"{a}: {id(a)}")


# because lists are mutalbe they suppport item assignment and the id remains the same
a[3] = 9
print(f"{a}: {id(a)}")


# MUTABLE OBJECTS IN PYTHON: lists, sets, dicts, custom classes
# IMMUTABLE OBJECTS IN PYTHON: int, float, string, tuple, bool, unicode

# python uses a refrence called "CALL BY OBJECT REFERENCE" which means that if the object is mutable it's call by reference and if the object is immutable it's call by value
# call by reference means that when you pass an mutable object to a function changing the object inside of function also changes the original object outside of function
# call by value only modifies immutable object inside of funciton


var = [1, 2, 3]


def change(var):

    # this is not changing the value it's creating a new local object
    # var = [1, 2, 3, 4]

    var.append(6)
    print("inside: ", var)


change(var)

print("outside: ", var)


# when you assign two immutables to the same object and value then they're the same and have the same id
a = "ali"
b = "ali"
print(a is b)

# for mutalbes even if they point to the same object and value they are different and have different id's (this works only if you pass them the same value, but if you say l1=l2 then they're the same untill one of them points to a new object)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)

# same as strings tuples are immutable and these two have the same id
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2)
