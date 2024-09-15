number = 0
while number ** 3 < 12_000:
    number += 1
    if number ** 3 > 12_000:
        print("The integer is", number - 1)
