import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\n--- Rock Paper Scissors Game ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print("Result:", result)

    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
