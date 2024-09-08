import  time

time = int(time.time())

ASCII_CODE = ord('A') + time % (ord('Z') - ord('A') + 1)
character = chr(ASCII_CODE)

print("The character of code", ASCII_CODE, "is ", character.upper())
