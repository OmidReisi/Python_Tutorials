# using context managers to open files is highly recommanded
# with context managers file is accessable through the indented block and you don't have to close it afterwards
with open(r"./Test/test_2.txt", "r") as f:
    print(f.name)
    print(f.mode)

# after the context manager block you actually have access to the file but you can't read from it or write to it
print(f.closed)
print(f.name)

# error file is closed
# print(f.read())
