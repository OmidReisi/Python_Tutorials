import calendar


# you can create your own custom calender with different start day with this method below
# inside the class constructor you pass the weekday that you want your calender to start with
my_cal = calendar.TextCalendar(calendar.SATURDAY)

# prmonth(year,month), pryear(year) prints the calendar for that given month or year
# my_cal.prmonth(2022, 1)
# my_cal.pryear(2022)

# these 2 methods return an string of the given month or year
jan = my_cal.formatmonth(2020, 4)
year_2020 = my_cal.formatyear(2020)

# all 4 methods above can take width(w) and length(l) as optional arguments as well

print(jan)
print(year_2020)
