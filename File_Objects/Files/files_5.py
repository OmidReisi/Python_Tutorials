with open(r"./Test/test_5.txt", "r") as f:

    # we can loop through lines of a file this way and there's no memory issue for large files
    # for line in f:
    #     print(line, end="")

    size_to_read = 10
    f_contents = f.read(size_to_read)

    print()

    # tell() returns the current position in file
    print("Position in file:", f.tell())

    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)

    print()
    print("Position in file:", f.tell())

    # seek() returns the file to set position and return the position
    print(f.seek(8))

    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f_contents)
