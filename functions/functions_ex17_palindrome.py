"""
    Write a function called is_palindrome. A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
"""
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(sentence):
    if [char.lower() for char in sentence if char != ' '] == [char.lower() for char in sentence[::-1] if char != ' ']:
        return True
    return False


print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('robert'))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('a man a plan a canal Panama'))

# Can be done MUCH simpler using string function .replace()


def is_palindrome(sentence):
    stripped = sentence.replace(" ", "").lower()
    return stripped == stripped[::-1]


print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('robert'))
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('a man a plan a canal Panama'))
