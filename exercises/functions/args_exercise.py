"""
    Define a function contains_purple that accepts any number of arguments. It should return True if any of the arguments are "purple" (all lowercase). Otherwise, it should return False
"""


def contains_purple(*args):
    if 'purple' in args:
        return True
    return False


print(contains_purple('something', 'bla', 2, 'four'))

print("Now I'll add something with purple...")

print(contains_purple('bla', 2, 5, 'second', 'purple'))
