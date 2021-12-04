class Open_File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # __enter__ and __exit__ are special methods that are invoked upon entering and exiting with statements respectively
    # you have to return your file object in __enter__ method so it's accessable inside with statement
    def __enter__(self):
        self.file = open(self.filename, self.mode)

        # print("exiting enter method")

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

        # print("exiting the exit method")


with Open_File(r"./sample.txt", "w") as f:

    # print("after enter method inside the body of with")

    f.write("Testing")

    # print("about to end the with statement before the exit method")

print(f.closed)

# print("after the exit method in the main body")
