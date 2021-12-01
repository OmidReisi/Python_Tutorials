import datetime
import pytz

dt_uctnow = datetime.datetime.now(tz=pytz.UTC)

print(dt_uctnow)

# astimezone method returns a new datetime with new timezone
# astimezone method only applies to timezone aware datetimes and can't be used on naive datetimes
# pytz.timezone returns the given timezone relavant to UTC
# both tz and zone can be passed as positional arguments as well
dt_mtn = dt_uctnow.astimezone(tz=pytz.timezone(zone="US/Mountain"))

print(dt_mtn)

print()
print()

# pytz.all_timezones returns a list of available timezones
# for tz in pytz.all_timezones:
#     print(tz)

dt_tehran = datetime.datetime.now(tz=pytz.timezone("Asia/Tehran"))

print(dt_tehran)


dt_iran = datetime.datetime.now(tz=pytz.timezone("Iran"))

print(dt_iran)

print()
print()


dt_iran_naive = datetime.datetime.now()

print(dt_iran_naive)

iran_tz = pytz.timezone("Iran")

# localize method of timezones takes a naive datetime and localize it based on the timezone
dt_iran_aware = iran_tz.localize(dt_iran_naive)

print(dt_iran_aware)

dt_iran_aware_2 = dt_iran_naive.replace(tzinfo=pytz.timezone("Asia/Tehran"))

print(dt_iran_aware_2)
