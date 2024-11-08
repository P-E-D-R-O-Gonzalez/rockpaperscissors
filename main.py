import random

# functions #
def get_choices():
	player_choice = input("Enter a choice (rock, paper, scissors): ")
	computer_choice = random.choice(["rock", "paper", "scissors"])
	choices = {"player" : player_choice, "computer" : computer_choice}
	return choices

def check_win(player, computer):
	print(f"you choose {player}, computer choose {computer}")
	if player == computer:
		return "It's a tie!"
	elif player == "rock":
		if computer == "scissors":
			return "Rock smashes scissors! You win!"
		else:
			return "Paper covers rock! You lose."
	elif player == "paper":
		if computer == "rock":
			return "Paper covers rock"
		else:
			return "scissors cuts paper! You lose."
	elif player == "scissors":
		if computer == "paper":
			return "scissors cuts paper! You Win!"
		else:
			return "Rock smashes scissors! You lose."


# main program #
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)