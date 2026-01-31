# ==========================================
# ROCK - PAPER - SCISSORS GAME IN PYTHON
# ==========================================

import random


# ----------- Function Definitions ----------

def display_rules():
    """Display game rules"""
    print("\n========== GAME RULES ==========")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("================================\n")


def get_user_choice():
    """Get user's choice with validation"""
    while True:
        print("Choose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            return "rock"
        elif choice == '2':
            return "paper"
        elif choice == '3':
            return "scissors"
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")


def get_computer_choice():
    """Generate computer choice"""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    """Determine the winner of a round"""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


def display_round_result(user, computer, winner):
    """Display result of the round"""
    print("\n-------------------------------")
    print(f"Your choice     : {user.capitalize()}")
    print(f"Computer choice : {computer.capitalize()}")

    if winner == "user":
        print("Result          : 🎉 You WIN this round!")
    elif winner == "computer":
        print("Result          : ❌ You LOSE this round!")
    else:
        print("Result          : 🤝 It's a TIE!")
    print("-------------------------------\n")


def display_score(user_score, computer_score):
    """Display current score"""
    print("Current Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    print("-------------------------------\n")


# -------------- Main Program ---------------

user_score = 0
computer_score = 0

print("==========================================")
print("     WELCOME TO ROCK PAPER SCISSORS")
print("==========================================")

display_rules()

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)

    display_round_result(user_choice, computer_choice, winner)

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    display_score(user_score, computer_score)

    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        print("\n==========================================")
        print("           GAME OVER")
        print("==========================================")
        print("Final Score")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        if user_score > computer_score:
            print("🏆 Congratulations! You won the game!")
        elif user_score < computer_score:
            print("😞 Computer wins the game!")
        else:
            print("🤝 The game is a tie!")

        print("\nThank you for playing!")
        break# ==========================================
# ROCK - PAPER - SCISSORS GAME IN PYTHON
# ==========================================

import random


# ----------- Function Definitions ----------

def display_rules():
    """Display game rules"""
    print("\n========== GAME RULES ==========")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("================================\n")


def get_user_choice():
    """Get user's choice with validation"""
    while True:
        print("Choose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            return "rock"
        elif choice == '2':
            return "paper"
        elif choice == '3':
            return "scissors"
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")


def get_computer_choice():
    """Generate computer choice"""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    """Determine the winner of a round"""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


def display_round_result(user, computer, winner):
    """Display result of the round"""
    print("\n-------------------------------")
    print(f"Your choice     : {user.capitalize()}")
    print(f"Computer choice : {computer.capitalize()}")

    if winner == "user":
        print("Result          : 🎉 You WIN this round!")
    elif winner == "computer":
        print("Result          : ❌ You LOSE this round!")
    else:
        print("Result          : 🤝 It's a TIE!")
    print("-------------------------------\n")


def display_score(user_score, computer_score):
    """Display current score"""
    print("Current Score")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    print("-------------------------------\n")


# -------------- Main Program ---------------

user_score = 0
computer_score = 0

print("==========================================")
print("     WELCOME TO ROCK PAPER SCISSORS")
print("==========================================")

display_rules()

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)

    display_round_result(user_choice, computer_choice, winner)

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    display_score(user_score, computer_score)

    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again != 'y':
        print("\n==========================================")
        print("           GAME OVER")
        print("==========================================")
        print("Final Score")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

        if user_score > computer_score:
            print("🏆 Congratulations! You won the game!")
        elif user_score < computer_score:
            print("😞 Computer wins the game!")
        else:
            print("🤝 The game is a tie!")

        print("\nThank you for playing!")
        break
