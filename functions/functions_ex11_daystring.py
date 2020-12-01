"""
    Write a function called return_day. This function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None. Hint: store the days of the week in a list (or dict using numbers as keys).
"""


def return_day(num):
    """Returns the string value of the numeric day of week. If input is not 1-7 the function returns None"""
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday',
            4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return days.get(num, None)
