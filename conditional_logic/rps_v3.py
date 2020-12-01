# My version with infinite looping and error handling
from random import randint

options = ["rock", "paper", "scissors"]
exit_flag = "Y"

while exit_flag == "Y":
    player = input("Enter your choice: \n").lower()
    ai_choice = randint(0, 2)

    print(f"Computer chose {options[ai_choice]}\n")

    if player in options:
        if player == options[ai_choice]:
            print("Draw!")
        elif (
            (player == "rock" and options[ai_choice] == "scissors")
            or (player == "scissors" and options[ai_choice] == "paper")
            or (player == "paper" and options[ai_choice] == "rock")
        ):

            print("\n*****You won!*****\n")
        else:
            print("You lost :(")
    else:
        print("You have to enter rock, paper or scissors...")

    exit_flag = input("Do you want to play another game? [Y|N]\n").upper()

    while exit_flag != "Y" and exit_flag != "N":
        exit_flag = input(
            "Sorry, I don't understand that. Please enter Y or N:\n").upper()

print("Thank you for playing!")
