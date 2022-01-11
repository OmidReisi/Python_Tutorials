import sys

# a string that shows the os (platform) that you're working with (for windows it's "win32")
print(sys.platform)

# a string that shows the python version and additional information such as build number and more.
print(sys.version)


a = 15
# this returns an integer showing the size of an object in bytes
print(sys.getsizeof(a))

# a list that shows the arguments you pass to python when you execute this script(usually it's just one item and it's the path to your current script)
# you can type multiple arguments after your script name and use this arguments in your program
print(sys.argv)


# you can type multiple arguments after your script name and use this arguments in your program ("python sys_1.py Omid 21" run this in terminal)
# print("Hi my name is {1} and I'm {2} years old.".format(*sys.argv))

# list of locations python looks for modules
print(sys.path)

# a string showing the path to the current python in use
print(sys.executable)
