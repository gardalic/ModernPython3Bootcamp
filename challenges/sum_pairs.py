"""
Write a function called sum_pairs which accepts a list and a number and returns the first pair of 
numbers that sum to the number passed to the function.
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
"""


def sum_pairs(lst, number):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            # print(f"{i} - {j}")
            if lst[i] + lst[j] >= number:  # If exact sum is needed, just do ==
                return [lst[i], lst[j]]
            else:
                j += 1
        i += 1
    return []


print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []
print(sum_pairs([1, 20, 4, 2, 1, 5], 25))
