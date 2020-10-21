"""
    Remove negative numbers from list.
"""


def remove_negatives(l):
    return list(filter(lambda x: x >= 0, l))


print(remove_negatives([-7,0,1,2,3,4,5]))
