"""
    Write a function called number_compare. This function takes in two parameters (both numbers). If the first is greater than the second, this function returns "First is greater" If the second number is greater than the first, the function returns "Second is greater" Otherwise the function returns "Numbers are equal"
"""
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    return "Numbers are equal"
