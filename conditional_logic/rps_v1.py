print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, make your move: ")
player2 = input("Player2, make your move: ")

if player1 and player2:
    if player1 == player2:
        print("Tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player1 won")
    elif player1 == "rock" and player2 == "paper":
        print("Player2 won")
    elif player1 == "paper" == player2 == "scissors":
        print("Player2 won")
    elif player1 == "paper" and player2 == "rock":
        print("Player1 won")
    elif player1 == "scissors" and player2 == "paper":
        print("Player1 won")
    elif player1 == "scissors" and player2 == "rock"::
        print("Player2 won")
    else: 
        print("Not a valid input")
else:
    print("Not a valid input")