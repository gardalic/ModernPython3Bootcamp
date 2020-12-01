print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, make your move: ")
player2 = input("Player2, make your move: ")

if player1 and player2:
    if player1 not in ("rock", "paper", "scissors") or player2 not in ("rock", "paper", "scissors"):
        print("Not a valid input, enter 'rock', 'paper' or 'scissors'!")
    elif player1 == player2:
        print("Tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player1 won")
        else:
            print("Player2 won")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player1 won")
        else:
            print("Player2 won")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player1 won")
        else: 
            print("Player2 won")
else:
    print("Not a valid input")