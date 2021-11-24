#  in write mode if the file doesn't exist already then it creats it automatically
# every time we run this module our files becomes empty at first because write method overwrites already existing files
with open(r"./Test/test_6.txt", "w") as f:

    # write() just like read() picks up right where it left off
    # this two lines writh two back to back Test in the file
    # f.write("Test")
    # f.write("Test")

    f.write("Test")

    # just like read(), write() also can use seek() to set the position for writing
    f.seek(0)

    f.write("Test")
