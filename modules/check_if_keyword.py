"""
    Define a function that will take any number of strings. Return True if any of the arguments are Python keywords, return False if none of the arguments are keywords.
    contains_keyword("hello", "goodbye")
    contains_keyword("def", "haha", "lol", "chicken", "alaska")
    contains_keyword("four", "for", "if")
    contains_keyword("blah", "doggo", "crab", "anchor")
"""
from keyword import iskeyword


def contains_keyword(*args):
    """If the argument contains keyword, return True. Otherwise return False. Function doctype test"""
    for arg in args:
        if iskeyword(arg):
            return True
    return False


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blah", "doggo", "crab", "anchor"))
