from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")
player_win = 0
comp_win = 0
winning_score = 3

while player_win < winning_score and comp_win < winning_score:
	print(f"Current score: player - {player_win}, computer - {comp_win}")
	player = input("Player, make your move: ").lower()
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"Computer plays {computer}" )

	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			player_win += 1
		else:
			print("computer wins!")
			comp_win += 1
	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			player_win += 1
		else:
			print("computer wins!")
			comp_win += 1
	elif player == "scissors":
		if computer == "paper":
			print("player wins!")
			player_win += 1
		else:
			print("computer wins!")
			comp_win += 1
	elif player.lower() == 'quit': 
		break
	else:
		print("Please enter a valid move!")

if player_win > comp_win:
	print("Player won!")
else:
	print("Computer won!")