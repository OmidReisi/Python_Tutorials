import datetime
import pytz

dt_tehran = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))

# this is the international format
print(dt_tehran.isoformat())

print()
print()


# datetime formating
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# this mehtod is used for datetime formating
print(dt_tehran.strftime("%B %d, %Y"))


dt_str = "November 30, 2021"

# this method parses a datetime object from a string
# you pass the string and the format it is in
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")

print(dt)


# strftime - Datetime to String
# strptime - String to Datetime
