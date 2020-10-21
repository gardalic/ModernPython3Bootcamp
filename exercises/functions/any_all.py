"""
    Implement a function is_all_strings that accepts a single iterable and returns True if it contains ONLY strings.  Otherwise, it should return false.  
"""
# is_all_strings([2,'a', 'b', 'c'])
# is_all_strings(['a', 'b', 'c'])


def is_all_strings(itrbl):
    # return all(ind == str(ind) for ind in itrbl)
    # Remember type() == str
    return all(type(ind) == str for ind in itrbl)


print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2, 'a', 'b', 'c']))
