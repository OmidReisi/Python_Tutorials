import csv

with open(r"./Test_Files/names.csv", "r", newline="") as read_file:

    csv_reader = csv.DictReader(read_file)

    # # using DictReader instead of csv.reader method returns a dictionary for each line with keys being the field names and values being the value of fields
    # # this class does not return the first line which is the field names because it usees them as dictionary keys
    # for line in csv_reader:
    #     print(line)
    # #     # print(line["email"])

    with open(r"./Test_Files/new_dict_names.csv", "w", newline="") as write_file:

        fieldnames = ["first_name", "last_name", "email"]

        # for DictWriter class you have to pass the fieldnames.
        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames, delimiter="\t")

        # writeheader method uses it's fieldnames attributes and writes the names of fields
        # you have to use this method to write the field names in DictWriter
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)