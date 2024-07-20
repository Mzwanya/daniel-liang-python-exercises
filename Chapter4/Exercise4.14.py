'''
4.14 (Game: heads or tails) Write a program that lets the user guess whether a flipped
coin displays the head or the tail. The program randomly generates an integer 0 or
1, which represents head or tail. The program prompts the user to enter a guess
and reports whether the guess is correct or incorrect.
'''
import random

guess = random.randint(0, 1)
answer = int(input("Enter guess, 0 = head, 1 = tail: "))

if guess == answer:
    print("Guess is correct")
else:
    print("Guess is incorrect")
