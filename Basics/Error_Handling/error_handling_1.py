# error_handling can have these four blocks below

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# this file does not exist so without try block this throws an error
# f = open("testfile.txt")

# try:
#     f = open("testfile.txt")

# except Exception:
#     print("Sorry, This file does not exist")


# we should be as specific as possible with exceptions so this is better than above
# we exit try block after the first exception occurs so we don't print continue try block here
try:
    f = open("testfile.txt")
    print("continue try block")

except FileNotFoundError:
    print("Sorry, This file does not exist")


# you can also print the error itself with this method
try:
    var = bad_var

except NameError as error:
    print(error)
