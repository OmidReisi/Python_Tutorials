import csv

with open(r"./Test_Files/names.csv", "r", newline="") as read_file:

    csv_reader = csv.DictReader(read_file)

    with open(r"./Test_Files/new_dict_names.csv", "w", newline="") as write_file:

        # we can pass only a part of our csv_file and remove some fields if we want to
        fieldnames = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()

        # here our new csv file only has the firs_name and last_name fields and we have removed the email field
        for line in csv_reader:

            csv_writer.writerow({key: line[key] for key in fieldnames})

            # we can do it this way if we want to as well
            # del line["email"]
            # csv_writer.writerow(line)
