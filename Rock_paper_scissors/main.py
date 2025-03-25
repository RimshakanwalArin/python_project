import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").strip().lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"
    else:
        return "You lost!"

def is_win(player, opponent):
    # Return True if player wins against opponent
    winning_combinations = {
        'r': 's',  # Rock beats Scissors
        's': 'p',  # Scissors beats Paper
        'p': 'r'   # Paper beats Rock
    }
    return opponent == winning_combinations[player]

# Uncomment to play the game
print(play())
