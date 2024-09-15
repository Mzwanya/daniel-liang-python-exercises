number = 0
while number * number < 12_000:
    number += 1
    if number * number > 12_000:
        print("The integer is", number)
