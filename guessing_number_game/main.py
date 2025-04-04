import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Yay! Congrats! You have guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c' and low <= high:
        guess = (low + high) // 2  # Binary search method for efficiency
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

    print(f"Yay! The computer guessed your number {guess} correctly!")

# Uncomment to play:
guess(10)
computer_guess(10)
