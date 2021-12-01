# for timezones we use pytz library

import datetime
import pytz

dt = datetime.datetime(2021, 11, 30, 9, 31, 35, 200000, tzinfo=pytz.UTC)

print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)

print(dt_now)

# utxnow method doesn't have a tzinfo argument but it returns a datetime object which it's tzinfo attribute can be replaced by a new value
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print(dt_utcnow)
