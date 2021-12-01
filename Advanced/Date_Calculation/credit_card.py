"""This program is used for calculating how long it would take to pay off the balance on a credit card.
"""

import datetime
import calendar

# balance to pay off
balance = 5000

# interest rate added to the remaining balance at the end of each year
interest_rate = 0.13

# the amount we pay off of our balance each month
monthly_payment = 500


today = datetime.date.today()

# # returns a tuple containing the day of the week for start of the month and how many days that month has
# start_of_month_and_days_in_month = calendar.monthrange(today.year, today.month)


# # today in november 30, 2021 and november 01, 2021 was a monday and november has 30 days so it returned (0,30)
# print(start_of_month_and_days_in_month)


days_in_current_month = calendar.monthrange(today.year, today.month)[1]

print(days_in_current_month)

days_till_end_of_current_month = days_in_current_month - today.day

print(days_till_end_of_current_month)

payment_start_date = today + datetime.timedelta(days=days_till_end_of_current_month + 1)

print(payment_start_date)


payment_end_date = payment_start_date

print()
print()

while balance > 0:

    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    # balance = round(balance, 2)
    # if balance < 0:
    #     balance = 0

    # we can use this instead of last 3 lines
    balance = 0 if balance < 0 else round(balance, 2)

    print(f"Date: {payment_end_date}\nBalance: {balance}\n\n")

    days_in_current_month = calendar.monthrange(
        payment_end_date.year, payment_end_date.month
    )[1]

    payment_end_date += datetime.timedelta(days=days_in_current_month)
