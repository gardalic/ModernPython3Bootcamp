"""
Write a function called two_list_dictionary which accepts two lists of varying lengths.The first list 
consists of keys and the second one consists of values. Your function should return a dictionary created 
from the keys and values. If there are not enough values, the remaining keys should have a value of null. 
If there not enough keys, just ignore the remaining values.

two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
"""


def two_list_dictionary(lst1, lst2):
    return_dict = {}
    for i, elem in enumerate(lst1):
        if i < len(lst2):
            return_dict[elem] = lst2[i]
        else:
            return_dict[elem] = None
    return return_dict


print(two_list_dictionary(["a", "b", "c"], [1, 2, 3, 4]))
