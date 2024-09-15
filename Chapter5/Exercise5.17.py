ASCII_CODE = ord('!')
count_per_line = 1
limit = 10
print("The characters in the ASCII character table are: ")
while ASCII_CODE <= ord('~'):
    print(str(chr(ASCII_CODE)), end=' ')
    if count_per_line % limit == 0:
        print()
    count_per_line += 1
    ASCII_CODE += 1
