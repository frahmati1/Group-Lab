# Game Instructions:

The game "Rock, Paper, Scissors" is played where each player simultaneously forms one of three shapes with an outstretched hand. The possible shapes are "rock" (a simple fist), "paper" (an open hand), and "scissors" (a fist with the index and middle fingers extended, forming a V). The rules are as follows:

Rock crushes scissors (rock wins)

Scissors cut paper (scissors win)

Paper covers rock (paper wins)

If both players choose the same shape, the game is tied, and they may play again.


# Game Algorithms:


    # Import the random module for generating random choices for the computer
     import random

    # Define the game function
    def rock_paper_scissors():
    # The choices available in the game
    choices = ['rock', 'paper', 'scissors']
    
    # Ask for the user's choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # The computer randomly selects its choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "User wins!"
    else:
        return "Computer wins!"

    # Play a round of the game
    result = rock_paper_scissors()
    print(result)

# Team member's roles:

- Farnoosh Rahmati - Product Owner/Business Analyst

Responsibilities:

•	Identifying business opportunities and potential project value.

•	Gathering, specifying, and prioritizing project requirements.

•	Communicating with stakeholders to ensure alignment with business objectives.

•	Estimating timeframes and overseeing the project's progress.


- Ashkan Rahmati - Lead Developer

Responsibilities:

•	Translating requirements and design mock-ups into functional code.

•	Leading the development team through coding sprints.

•	Reviewing code, integrating work, and ensuring the technical quality of the product.

•	Collaborating with the Product Owner to refine features and iterations.


- Amin Ameli Kalkhoran - QA Lead/Test Engineer

Responsibilities:

•	Developing test plans and test cases to ensure software functionality.

•	Executing tests, documenting results, and identifying defects.

•	Collaborating with the development team to troubleshoot and resolve issues.

•	Overseeing final deployment of the product to production and ensuring quality standards are met.
