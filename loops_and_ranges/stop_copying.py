# Repeat input until 'Stop copying me' is entered

phrase = input("Hey, how is it going? ")

while phrase.lower().strip() != 'stop copying me':
    print(phrase)
    phrase = input()

print("Fine...")
