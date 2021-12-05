# as shown below we can do this without csv module as well but it is better to use the module
with open(r"./Test_Files/names.csv", "r") as read_file:
    with open(r"./Test_Files/renames.csv", "w") as write_file:
        for line in read_file:
            write_file.write(line.replace(",", ";"))
            
