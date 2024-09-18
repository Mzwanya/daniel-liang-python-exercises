import random

guess_digit1 = lottery_digit1 = random.randint(0, 9)
lottery_digit2 = random.randint(0, 9)

while lottery_digit1 == lottery_digit2:
    lottery_digit2 = random.randint(0, 9)

guess = eval(input("Enter your lottery pick (two digits): "))

guess_digit1 = guess // 10
guess_digit2 = guess % 10

print("The lottery number is ", lottery_digit1, lottery_digit2)

if guess_digit1 == lottery_digit1 and guess_digit2 == lottery_digit2:
    print("Exact match: you win $10,000")
elif guess_digit2 == lottery_digit1 and guess_digit1 == lottery_digit2:
    print("Match all digits: you win $3,000")
elif (guess_digit1 == lottery_digit1
      or guess_digit1 == lottery_digit2
      or guess_digit2 == lottery_digit1
      or guess_digit2 == lottery_digit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
