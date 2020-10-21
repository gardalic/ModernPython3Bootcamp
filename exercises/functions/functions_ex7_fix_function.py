"""
    The pre-written function is broken. It's supposed to return the number of $  characters in a given string. For example: count_dollar_signs("$uper $ize") should return 2. But for some reason, the function always returns either 0 or 1. What's going on?

    Original function:
    def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count
"""

# Without adding any new lines of code, make count_dollar_signs work as intended


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count  # issue was here, return inside the for loop


print(count_dollar_signs("$uper $ize"))
