from datetime import datetime


def count_days(day1: str, day2: str) -> int:
    """count days"""
    # convert string to date object
    d1 = datetime.strptime(day1, "%Y-%m-%d")
    d2 = datetime.strptime(day2, "%Y-%m-%d")

    # difference between dates in timedelta
    delta = d2 - d1
    print(f'Difference is {delta.days + 1} days')
    return delta.days + 1


# a = '2023-01-01'
# b = '2023-01-24'
# count_days(a, b)
