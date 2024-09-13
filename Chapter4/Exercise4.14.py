# Game: heads or tails
import random

guess = random.randint(0, 1)
answer = int(input("Enter guess, 0 = head, 1 = tail: "))

if guess == answer:
    print("Guess is correct!")
else:
    print("Guess is incorrect. Correct guess is ", end="Head!" if guess == 0 else "Tail")
