# Guess a number between 1 and 10
# Computer gives feedback if the number is too low or too high
# Computer asks if the player wants to keep going (y/n)

from random import randint

number = randint(1, 10)
exit_flag = 'y'

while exit_flag.lower() != 'n':
    guess = input("Guess a number (1-10): ")

    try:
        guess = int(guess)
    except ValueError:
        print("Not a number")
        continue

    if guess < 1 or guess > 10:
        print("Guess is not between 1 and 10")
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print(f"Good job! The number was {number}")
        exit_flag = input("Do you want to play another game (y/n)? ")

        while exit_flag.lower() not in ('y', 'n'):
            print("Sorry, I didn't get that...")
            exit_flag = input("Do you want to play another game (y/n)? ")

        number = randint(1, 10)
print("Thank you for playing!")
