import calendar


# takes the first day of the week as it's argument and creats a calendar with html tags for using in web
html_cal = calendar.HTMLCalendar(calendar.SATURDAY)

# returns an html table as a string for that month
# if withyear argument is set to False then it doesn't show the year number(default is True)
print(html_cal.formatmonth(2022, 1))

# you can also pass a width argument for this method
print(html_cal.formatyear(2022, width=5))
