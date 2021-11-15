#  number of days in each month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):

    """Return True for leap years, False fo non-leap years.

    Args:
        year (int): shows the selected year in A.D
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    """Return number of days in that month in the year/

    Args:
        year (int): shows the selected year in A.D
        month (int): shows the selected month in number
    """
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(days_in_month(2020, 2))
print(days_in_month(2021, 11))

print(is_leap(2020))
print(is_leap(2021))
