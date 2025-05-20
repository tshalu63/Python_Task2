import random

def get_user_choice():
    choice = input("Enter Rock, Paper or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
        choice = input("Enter Rock, Paper or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a draw!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("=== Welcome to Rock, Paper, Scissors Game ===")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

play_game()