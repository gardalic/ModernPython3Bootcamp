"""
    Write a function called generate_evens that returns a list of the even numbers between 1 and 50 (not including 50). Basically, it should return a list: [2,4,6....all the way up to 48]. Inside the function, you can construct the list using either a loop OR list comprehension. You do not need to call the function in this exercise, defining it is enough.
"""


def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0 ]
