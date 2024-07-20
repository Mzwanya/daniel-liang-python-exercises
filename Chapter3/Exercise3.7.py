import  time

time = int(time.time())

ascii_code = time % 100 + 65

character = chr(ascii_code)

print("The character of code", ascii_code, "is ", character.upper())