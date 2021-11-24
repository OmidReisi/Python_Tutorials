with open(r"./Test/test_7.txt", "r") as read_file:
    with open(r"./Test/test_7_copy.txt", "w") as write_file:

        # this is not recommanded for big files
        # write_file.write(read_file.read())

        # this way is better cause we don't read all of the file at the same time
        for line in read_file:
            write_file.write(line)
