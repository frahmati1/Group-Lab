mport random

options = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(options)

print(f"You chose {user_choice}, and the computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("You lose!")


