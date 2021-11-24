# open function is used for accessing files
# files open on different modes but if nothing is passed then default is reading mode but it's better to be explicit
f = open(r"./Test/test_1.txt", mode="r")

# name of the file
print(f.name)

print(f.mode)


# if no context manager is used then we have to explicitly close the file
f.close()
