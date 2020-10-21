from random import randint

choice = randint(1, 10)

if choice == 7:
    print(f"{choice} - lucky")
else:
    print(f"{choice} - unlucky")
