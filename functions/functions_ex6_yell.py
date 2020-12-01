# Create a function that returns (doesn't print, but you can do that later) an uppercased version of a passed argument, with an exclamation point added to the end.

def yell(phrase):
    return f"{phrase.upper()}!"


print(yell("test phrase"))
