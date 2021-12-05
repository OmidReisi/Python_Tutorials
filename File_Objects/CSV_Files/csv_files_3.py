import csv

with open(r"./Test_Files/names.csv", "r", newline="") as read_file:

    # if we pass the wrong delimiter in reading csv_files then the reader method does'nt reacognizes the fields and returns each line as only one field
    # the default delimiter is ,
    csv_reader = csv.reader(read_file, delimiter=",")

    # # here we passed the wrong delimiter and got several lists with only one value
    # for line in csv_reader:
    #     print(line)

    with open(r"./Test_Files/new_names.csv", "w", newline="") as write_file:

        # delimiter is a keyword argument (can't be a positional argument has to be passed as keyword delimiter) that represents field seperators
        # if no delimiter is passed then the default is ,
        csv_writer = csv.writer(write_file, delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)
