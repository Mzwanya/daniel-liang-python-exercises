''' *5.17 (Display the ASCII character table) Write a program that displays the characters
in the ASCII character table from ! to ~. Display ten characters per line.
The characters are separated by exactly one space
'''

ASCII_CODE = 33
count_per_line = 1
limit = 10
print("The characters in the ASCII character table are: ")
while ASCII_CODE <= 126:
    print(str(chr(ASCII_CODE)), end=' ')
    if count_per_line % limit == 0:
        print()
    count_per_line += 1
    ASCII_CODE += 1
