# Write a function called intersection. The function should accept two lists and return a list with the values that are in both input lists

def intersection(lst1, lst2):
    # write without using &
    return [elem for elem in lst1 if elem in lst2]
