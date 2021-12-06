import csv


html_output = ""
names = []

with open(r"./Patrons.csv", "r", newline="") as data_file:
    csv_data = csv.DictReader(data_file)

    next(csv_data)

    for line in csv_data:

        if line["FirstName"] == "No Reward":
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<ol>{name}</ol>"


html_output += "\n</ul>"

print(html_output)
