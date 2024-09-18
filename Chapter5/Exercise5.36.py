# Game: scissor, rock, paper

import random
import sys

count = 0
while count <= 2 or count <= -2:

    # Generate scissor, rock, or paper
    computer_id = random.randint(0, 2)

    # Prompt the user to enter scissor, rock, or paper
    player_id = int(input("scissor (0), rock (1), paper (2): "))

    computer = ''
    player = ''

    if computer_id == 0:
        computer = 'scissor'
    elif computer_id == 1:
        computer = 'rock'
    else:
        computer = 'paper'

    if player_id == 0:
        player = 'scissor'
    elif player_id == 1:
        player = 'rock'
    elif player_id == 2:
        player = 'paper'
    else:
        sys.exit("Error: invalid input!")

    # Check the guess
    if player == computer:
        print(f"The computer is {computer}. you are {player} too. It is a draw.")
    elif player == 'rock':
        if computer == 'scissor':
            print("The computer is scissor. you are rock. You won.")
            count += 1
        else:             # computer == 'paper'
            print("The computer is paper. you are rock. You lose.")
            count -= 1
    elif player == 'scissor':
        if computer == 'rock':
            print("The computer is rock. you are scissor. You lose.")
            count -= 1
        else:             # computer == 'paper'
            print("The computer is paper. you are scissor. You won.")
            count += 1
    else:                 # user == 'paper'
        if computer == 'rock':
            print("The computer is rock. you are paper. You won.")
            count += 1
        else:             # computer == 'scissor'
            print("The computer is scissor. you are paper. You lose.")
            count -= 1

if count > 2:
    print("You won more than two times!")
else:
    print("The computer won more than two times!")
