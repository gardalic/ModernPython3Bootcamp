"""
    Given the string "amazing", create a variable called "answer", which is a list containing all the letters from "amazing" but not the vowels (a, e, i, o, and u).  The answer should look like: ['m', 'z', 'n', 'g'].
"""
answer = [x for x in list("amazing") if x not in ["a", "e", "i", "o", "u"]] # list("amazing") not needed, could have been just "amazing"
print(answer)
