"""
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
"""


def find_and_replace(file, old, new):
    with open(file) as f:
        text = f.read()
    with open(file, "w") as f:
        f.write(text.replace(old, new))
