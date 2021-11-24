with open(r"./Test/test_3.txt", "r") as f:

    # read() returns all the contents of a file
    # f_contents = f.read()
    # print(f_contents)

    # read first 100 characters of a file
    f_contents = f.read(100)
    print(f_contents, end="")

    print()

    # like generators files pick up right were they left off
    f_contents = f.read(100)
    print(f_contents, end="")

    print()

    # this prints an empty string becaue the file is over
    f_contents = f.read(100)
    print(f_contents, end="")
