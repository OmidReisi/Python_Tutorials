import datetime

my_date = datetime.datetime(2021, 11, 23, 16, 50, 30, 700000)

print(my_date)

sentence = f"{my_date:%B %d, %Y}"
print(sentence)


sentence = (
    f"{my_date:%B %d, %Y} fell on a {my_date:%A} and was the {my_date:%j} of the year"
)

print(sentence)


# datetime formating
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
