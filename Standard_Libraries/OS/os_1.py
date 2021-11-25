import os

# prints everything that is available in os module
# print(dir(os))

# prints current working directory
print(os.getcwd())

# changes the current working directory to the given path
# os.chdir(r"../../")
# print(os.getcwd())

# returns a list of every file and folder in the given path (if no path is given uses the current working directory instead)
print(os.listdir())

# prints the location of the library
# works for self created modules as well
print(os.__file__)


# create a new directory in the given path but does not create in between folders
# os.mkdir()

# same as os.mkdir() but also creates in between folders
# os.makedirs()

# same as above the later removes in between directories as well
# non of them delete non-empty folders
# os.rmdir()
# os.removedirs()

# os.makedirs(r"./Test_1/Test_2/Test_3")

# this removes all the  Test_1, Test_2 and Test_3 folders
# does not delete the non-empty folders
# os.removedirs(r"./Test_1/Test_2/Test_3")

# renames the given file it's name
# os.rename(r"./Test/test_1.txt", r"./Test/text_1_renamed.txt")

# return the given file it's details
# print(os.stat(r"./Test/text_1_renamed.txt"))
# print(os.stat(r"./Test/text_1_renamed.txt").st_size)


# it is a generator that yields a 3-tuple in each turn
# it works like a depth firt ltr(left to right) tree (top to down and then left to right)
# for dirpath, dirnames, filenames in os.walk(r"../../"):

#     print("Current Path:", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)


# print(os.environ["Home"])
print(os.environ.get("Home"))

file_path = os.environ.get("Home")

# all of os.path methods that are used below can work on non existing paths

# returns a joined path of two paths together so you don't have to worry about forgetting a /
print(os.path.join(file_path, "test.txt"))

print()
print()

# returns the full name
print(os.path.basename(r"./Test/text_1_renamed.txt"))

# returns the path to the directory of file
print(os.path.dirname(r"./Test/text_1_renamed.txt"))

# returns both fullname and path to directory in a tuple
print(os.path.split(r"./Test/text_1_renamed.txt"))

# to check if the given path is real
print(os.path.exists(r"./Test/text_1_renamed.txt"))


# the following works only on existing paths

print()
print()


# to see if it's a directory
print(os.path.isdir(r"./Test/"))

# to see if it's a file
print(os.path.isfile(r"./Test/text_1_renamed.txt"))

# splits the file_name and it's path from it's extension into a tuple
print(os.path.splitext(r"./Test/text_1_renamed.txt"))

# returns the relative path of the given address from the current working directory
print(os.path.relpath(r"./"))

# prints the full path of the given address
print(os.path.realpath(r"./"))
