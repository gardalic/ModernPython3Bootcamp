# Generate a random number until the number generated is 5

from random import randint

number = 0
try_counter = 0

while number != 5:
    number = randint(1, 10)
    try_counter += 1

    if number == 5:
        print("Bingo!")
    else:
        print(f"The number generated is {number}, not 5")

print(f"It took {try_counter} tries to get to 5")
