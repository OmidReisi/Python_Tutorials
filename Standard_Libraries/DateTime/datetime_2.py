import datetime

# returns the current local datetime with no timezone (you can't pass a timezone to this method)
dt_today = datetime.datetime.today()

# same as above but with ability to pass timezone
# out of this three methods only this one can be time zone aware if we pass a timezone to it
dt_now = datetime.datetime.now()

# returns the current utc time but the timezone is still empty
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)

print(dt_now)

print(dt_utcnow)
