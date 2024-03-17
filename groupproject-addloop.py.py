import random

def rock_paper_scissors():
    while True:
        choices = ['rock', 'paper', 'scissors']
        computer_option = random.choice(choices)
        user_option = input("Choose rock, paper, or scissors: ").lower()

        if user_option not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        if user_option == computer_option:
            print(f"It's a tie! Both chose {user_option}.")
        elif (user_option == 'rock' and computer_option == 'scissors') \
            or (user_option == 'paper' and computer_option == 'rock') \
            or (user_option == 'scissors' and computer_option == 'paper'):
            print(f"You win! Computer chose {computer_option}.")
        else:
            print(f"You lose! Computer chose {computer_option}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break  
        break
        # exit
        

if __name__ == "__main__":
    rock_paper_scissors()
    