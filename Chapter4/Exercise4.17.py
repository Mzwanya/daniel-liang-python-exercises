# Game: scissor, rock, paper

import random
import sys

computer_id = random.randint(0, 2)
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

if player == computer:
    print(f"The computer is {computer}. you are {player} too. It is a draw.")
elif player == 'rock':
    if computer == 'scissor':
        print("The computer is scissor. you are rock. You won.")
    else:             # computer == 'paper'
        print("The computer is paper. you are rock. You lose.")
elif player == 'scissor':
    if computer == 'rock':
        print("The computer is rock. you are scissor. You lose.")
    else:             # computer == 'paper'
        print("The computer is paper. you are scissor. You won.")
else:                 # user == 'paper'
    if computer == 'rock':
        print("The computer is rock. you are paper. You won.")
    else:             # computer == 'scissor'
        print("The computer is scissor. you are paper. You lose.")
