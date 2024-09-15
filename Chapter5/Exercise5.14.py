number = 0
while number ** 2 < 12_000:
    number += 1
    if number ** 2 > 12_000:
        print("The integer is", number)
