# *5.20 (Display four patterns using loops) Use nested loops that display the following
# patterns in four separate programs:

number_of_lines = 6

# NOTE: Run each of this program in pieces (Pattern A, B, C, D) seperately. You can use block comments (''' ''')
# Otherwise if you run them all at once pattern D wont be printed out.

# Pattern A

count = 1
print("Pattern A:")
for i in range(number_of_lines + 1):
    for j in range(1, count):
        print(j, end=' ')
    count += 1
    print()

# Pattern B

print("Pattern B:")
count = 6
for m in range(number_of_lines + 1):
    for n in range(1, count + 1):
        print(n, end=' ')
    count -= 1
    print()
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
print('\n')
# Pattern D
print()
print("Pattern D:")
count = 6
for x in range(number_of_lines + 1):
    for y in range(1, count + 1):
        print(y, end=' ')
    count -= 1
    print()
