import datetime

# naive dates and times don't have timezones and daylight savings times
# aware dates and times do have timezones and daylight savings times.


# date takes only year, month and day with normal integers (don't zero pad the arguments)
d = datetime.date(2021, 11, 29)
print(d)

tday = datetime.date.today()
print(tday)

# date objects have year, month and day attributes
print(tday.year)

# both return the day of the week and monday is the first day but weekday starts at 0 and isoweekday starts at 1
print(tday.weekday())
print(tday.isoweekday())


# timedelta is just the difference between two dates or times
tdelta = datetime.timedelta(days=7)
print(tdelta)

print()
print()

print(tday + tdelta)


# date2 = date1 +/- timedelta
# timedelta = date2 - date1

# adding two datetime objects results in an error

bday = datetime.date(2022, 8, 30)

# this returns a timedelta object
till_bday = bday - tday

print(till_bday.days)
# returns the timedelta in seconds
print(till_bday.total_seconds())

print()
print()

# time takes hour(in 24 hour format), minute, seconds, microseconds and tzinfo
t = datetime.time(15, 1, 20, 300000)
print(t)
print(t.hour)


print()
print()

# datetime object contains both date and time
dt = datetime.datetime(2021, 11, 29, 15, 4, 25, 300000)
print(dt)
print(dt.year)

# returns time portion of datetime
print(dt.time())

# return date portion of datetime
print(dt.date())

tdelta = datetime.timedelta(hours=12)

print(dt + tdelta)
