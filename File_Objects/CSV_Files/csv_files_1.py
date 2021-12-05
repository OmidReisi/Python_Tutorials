# csv files are just text files that have different fields seperated with a delimiter (usually a ,) like plain excel files

import csv

# because of windows \n problems you should always open csv_file with new_line = ""
with open(r"./Test_Files/names.csv", "r", newline="") as csv_file:
    # reader method returns an iterator which contains each line of the file as a seperate list
    csv_reader = csv.reader(csv_file)

    # print(csv_reader)

    # in order to skip the fields names
    next(csv_reader)

    for line in csv_reader:
        print(line)
