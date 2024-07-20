'''
*4.17 (Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-paper game. (A scissor can cut a paper, a rock can knock a scissor,
and a paper can wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.




# MY COMMENT: I found this game really funny. Lol

'''

import random
import sys

computer_number = random.randint(0, 2)
if computer_number == 0:
    computer = 'scissor'
elif computer_number == 1:
    computer = 'rock'
else:
     computer = 'paper'

user_number = int(input("scissor (0), rock (1), paper (2): "))
if user_number == 0:
    user = 'scissor'
elif user_number == 1:
    user = 'rock'
elif user_number == 2:
    user = 'paper'
else:
    print("Error: invalid input!")
    sys.exit()

if user == computer:
    print(f"The computer is {computer}. you are {user} too. It is a draw.")
elif user == 'rock':
    if computer == 'scissor':
        print(f"The computer is {computer}. you are {user}. You won.")
    else:             # computer == 'paper'
        print(f"The computer is {computer}. you are {user}. You lose.")
elif user == 'scissor':
    if computer == 'rock':
        print(f"The computer is {computer}. you are {user}. You lose.")
    else:             # computer == 'paper'
        print(f"The computer is {computer}. you are {user}. You won.")
else:                 # user == 'paper'
    if computer == 'rock':
        print(f"The computer is {computer}. you are {user}. You won.")
    else:             # computer == 'scissor'
        print(f"The computer is {computer}. you are {user}. You lose.")