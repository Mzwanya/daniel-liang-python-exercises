# Game: scissor, rock, paper

import random

user_score = 0
computer_score = 0

# Play the game until either the user or the computer wins more than two time
while user_score <= 2 and computer_score <= 2:
    # Computer randomly chooses a number between 0 and 2
    computer_input = random.randint(0, 2)

     # Ask user to input their choice
    user_input = int(input("scissor (0), rock (1), paper (2): "))

    # Determine the winner based on the rules of the game
    if user_input == computer_input:
        print("It's a draw!\n")
    elif (user_input == 0 and computer_input == 2) or \
         (user_input == 1 and computer_input == 0) or \
         (user_input == 2 and computer_input == 1):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1
    
    # Display the current scores
    print(f"Current Scores - You: {user_score}, Computer: {computer_score}\n")

# Final result
if user_score > 2:
    print("Congratulations! You won the game!")
else:
    print("Computer won the game! Better luck next time!")
