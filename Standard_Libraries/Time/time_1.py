import time

# epoch is the time that your computer considers start of the time (depending on the system it's usually somewhere around january 1, 1970)

# ctime takes an argument that specifies the total seconds that have passes since epoch and returns a string that shows the date of those seconds
# you can see your systems epoch by passing 0 to the ctime method
print(time.ctime(0))

# returns the total seconds passed from the epoch to the current time of your system
print(time.time())

# convert the given seconds from the epoch to a time object
# if no argument is passed convert the current time
# time.gmtime() works just like local time instead it returns the time object in UTC timezone and dst_flag is always 0
time_obj = time.localtime()

print(time_obj)

# these two methods work the same way as they do in datetime module(strftime takes the time_object after it's format)
# for formatting read the documentation: https://docs.python.org/3/library/time.html#time.strftime
# if you want to remove zero padding use a "#" between the % and the letter (for example %#d)
time_str = time.strftime("%A, %B %#d, %Y", time_obj)
print(time_str)

# the fomat you pass in should be the exact format that the str_time is in (you don't need to pass # if you've used it to remove zero padding)
time_obj = time.strptime(time_str, "%A, %B %d, %Y")
print(time_obj)
