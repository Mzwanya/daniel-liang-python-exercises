'''
**4.15 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
2. If all the digits in the user input match all the digits in the lottery number, the
award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is
$1,000.

MY COMMENT (or Observation. Perhaps I maybe wrong): The program generates random integers from 0 to 99 ( Listing 4.10, Lottery.py). The problem with this is that the user
is requested to only enter a two digit integer, that is, integers from 10 to 99 leaving the first integers (single integers, 0 to 9), yet, as it can
be seen the the program has a possibility to generate single digit integers as well, which is an unfair game.
To avoid this, I have modified the program (This program), not just to prompt the user to guess a three digit integer but also the random function to generate
exactly three digits, that is, from 100 to 999 in each prompt, and not from 0 to 999.
Also, if the user input does not match rules 1 and 2, there is a possibility that two or one digit in the user input matches in the lottery number, not only
one digit as opposed to rule 3 above.
'''
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

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guess_digit1 == lottery_digit1 or guess_digit1 == lottery_digit2 or guess_digit1 == lottery_digit3) and \
        (guess_digit2 == lottery_digit1 or guess_digit2 == lottery_digit2 or guess_digit2 == lottery_digit3) and \
        (guess_digit3 == lottery_digit1 or guess_digit3 == lottery_digit2 or guess_digit3 == lottery_digit3):
    print("Match all digits: you win $3,000")
elif (guess_digit1 == lottery_digit1 or guess_digit1 == lottery_digit2 or guess_digit1 == lottery_digit3) or \
        (guess_digit2 == lottery_digit2 or guess_digit2 == lottery_digit3) or \
        (guess_digit3 == lottery_digit3):
    print("Match one or two digit: you win $1,000")
else:
    print("Sorry, no match")
