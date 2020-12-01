"""   
    Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!
"""
vowels = "aeiou"
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {vowels[i]: 0 for i in range(0, len(vowels))}
print(answer)

# simpler solution
answer = {char: 0 for char in 'aeiou'}
print(answer)

# OR even simpler
answer = dict.fromkeys('aeiou', 0)
print(answer)
