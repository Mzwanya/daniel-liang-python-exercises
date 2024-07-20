# TO BE CONTINUED...


limit = 9
count = 0
power = count
spaces = limit * 3
for i in range(limit):
    print('  ' * spaces, end='  ')
    for k in range(0, count):
        print(2 ** k, end='   ')
    power = count - 2
    for m in range(1, count):
        print(2 ** power, end='   ')
        power -= 1
    if i <= 4:
        spaces -= 2
    else:
        spaces -= 3
    print()
    count += 1
