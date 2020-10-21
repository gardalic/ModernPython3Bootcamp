"""
    Write a function called speak that accepts a single parameter, animal. 
    If animal is "pig", it should return "oink". If animal is "duck", it should return "quack". If animal is "cat", it should return "meow".If animal is "dog", it should return "woof". If animal is anything else, it should return "?". If no animal is specified, it should default to "dog"
"""


def speak(animal="dog"):
    if animal.lower() == "pig":
        return "oink"
    elif animal.lower() == "duck":
        return "quack"
    elif animal.lower() == "cat":
        return "meow"
    elif animal.lower() == "dog":
        return "woof"
    return "?"

# ALTERNATIVE
# Can use predefined list in a dictionary


def speak_2(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:  # with .get() if there is no key None is returned. None is False
        return noise
    return "?"


# Even simpler, pass default to .get()
def speak(animal='dog'):
    noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
    return noises.get(animal, '?')
