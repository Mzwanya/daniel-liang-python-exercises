# Game: lottery
import random

# Generate a lottery number
lottery = random.randint(100, 999)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

print("The lottery number is", lottery)

# Get digits from lottery
lottery_digit1 = lottery // 100
lottery_digit2 = lottery // 10 % 10
lottery_digit3 = lottery % 10

# Get digits from guess
guess_digit1 = guess // 100
guess_digit2 = guess // 10 % 10
guess_digit3 = guess % 10

# Check the guess and display the results
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guess_digit1 == lottery_digit1 or guess_digit1 == lottery_digit2 or guess_digit1 == lottery_digit3) and \
        (guess_digit2 == lottery_digit1 or guess_digit2 == lottery_digit2 or guess_digit2 == lottery_digit3) and \
        (guess_digit3 == lottery_digit1 or guess_digit3 == lottery_digit2 or guess_digit3 == lottery_digit3):
    print("Match all digits: you win $3,000")
elif (guess_digit1 == lottery_digit1 or guess_digit1 == lottery_digit2 or guess_digit1 == lottery_digit3) or \
        (guess_digit2 == lottery_digit2 or guess_digit2 == lottery_digit3) or \
        (guess_digit3 == lottery_digit3):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
