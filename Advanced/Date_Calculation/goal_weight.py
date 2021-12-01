"""This program calculates how long it would take to get to our goal weight
"""

import datetime

# current weight in pounds
current_weight = 220

# goal weight in pounds
goal_weight = 180

# average weekly weight loss in pounds
avg_lbs_week = 1.5


start_date = datetime.date.today()
end_date = start_date


while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week


print(f"Reached goal in : {(end_date - start_date).days // 7} weeks")
print(f"Date : {end_date}")
