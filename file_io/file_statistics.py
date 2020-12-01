"""Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file."""

# statistics('story.txt') # {'lines': 172, 'words': 2145, 'characters': 11227}


def statistics(file):
    with open(file) as f:
        lines = f.readlines()

    words, characters = 0, 0
    for line in lines:
        words += len(line.split())
        characters += len(line)

    stats = {"lines": len(lines), "words": words, "characters": characters}
    return stats

# More Pythonic - not sure about resource consumption
# words = sum(len(line) for line in lines)
# characters = sum(len(line) for line in lines)
