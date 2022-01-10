import calendar


# returns True if the given year is leap else False
print(calendar.isleap(2020))

# returns a multiline string representing the calender of the given month with the given year
# w is width of the calendar month(default is 1)
# l is  length (height) of the calendar month(default is 1)
# all arguments can be passed as positional arguments as well
jan = calendar.month(theyear=2022, themonth=1, w=4, l=3)
print(jan)

# # this returns the year's calendar as a multiline string(you can also specify width and length of each month of the calendar as well)
# year_2022 = calendar.calendar(2022)
# print(year_2022)

# # returns an integer (0,6) for the given year, month and day (monday is 0)
# print(calendar.weekday(2022, 1, 9))

# # returns an integer representing the number of leap years between [y1,y2)
# print(calendar.leapdays(2000, 2020))

# # returns a matrix (list of lists) with each list representing a week of the given month and year
# # the position of each element is it's weekday (this means the elemnts that are zero are not in this month)
# # this means that january of 2022 started on s saturday
# print(calendar.monthcalendar(2022, 1))


# # returns a tuple containing the day of the week for start of the month and how many days that month has
# start_of_month_and_days_in_month = calendar.monthrange(2022, 1)


# # this means that january of 2022 started on a saturday (5) and it has 31 days
# print(start_of_month_and_days_in_month)

# this returns a string of weekday names based on the integer it gets
# 1: M T W T F S S
# 2: Mo Tu We Th Fr Sa Su
# 3: Mon Tue Wed Thu Fri Sat Sun
# 9: Monday   Tuesday  Wednesday  Thursday   Friday   Saturday   Sunday
# any other number just adds space between the names (use only these 4 numbers)
print(calendar.weekheader(9))

# this returns an iterator of month names in 3 letters (first element is empty so the month number matches the position in sequence)
print(list(calendar.month_abbr))
# same as above but month have their full names
print(list(calendar.month_name))

# both return iterators of days (3 letter days and fullname days)
print(list(calendar.day_abbr))
print(list(calendar.day_name))
