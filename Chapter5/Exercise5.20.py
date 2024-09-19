number_of_lines = 6

# Pattern A
count = 1
print("Pattern A:")
for i in range(number_of_lines + 1):
    for j in range(1, count):
        print(j, end=' ')
    count += 1
    print()
print("\n")

# Pattern B
print("Pattern B:")
count = 6
for m in range(number_of_lines + 1):
    for n in range(1, count + 1):
        print(n, end=' ')
    count -= 1
    print()
print("\n")

# Pattern C
print("Pattern C:")
count = 1
spaces = 12
for h in range(number_of_lines + 1):
    print(' ' * spaces, end='')
    for k in range(1, count):
        print(-k + h + 1, end=' ')
    count += 1
    spaces -= 2
    number_of_lines -= 1
    print()
print("\n")

# Reset number_of_lines to ensure correct output for Pattern D
number_of_lines = 6

# Pattern D
print("Pattern D:")
count = 6
for x in range(number_of_lines + 1):
    for y in range(1, count + 1):
        print(y, end=' ')
    count -= 1
    print()
