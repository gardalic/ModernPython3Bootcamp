"""
    Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.
"""
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(lst):
    product = 1
    flag = False
    for num in lst:
        if num % 2 == 0:
            product *= num
            flag = True
    if flag:
        return product
    return 0


print(multiply_even_numbers([2, 3, 4, 5, 6]))
