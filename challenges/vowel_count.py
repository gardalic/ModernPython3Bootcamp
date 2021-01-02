'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(word):
    vowels = "aeiou"
    count = {}
    for letter in word.lower():
        if letter in vowels:
            count[letter] = count.get(letter, 0) + 1
    return count

# Solution can be simple .count() - strin has count function
# {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

print(vowel_count('awesome'))