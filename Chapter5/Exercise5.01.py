negatives = 0
positives = 0
total = 0
integer = int(input("Enter an integer, the input ends if you enter 0: "))
if integer == 0:
    print("You didn't enter an any number.")
else:
    while integer != 0:
        if integer > 0:
            positives += 1
        else:
            negatives += 1
        total += integer
        integer = int(input("Enter an integer, the input ends if you enter 0: "))
    average = total / (negatives + positives)
    print("The number of positives is", positives, '\n' + \
          "The number of negatives is", negatives, '\n' + \
            "The total is", total, '\n' + \
                "The average is", average)
    