# 4.16 (Random character) Write a program that displays a random uppercase letter.

import random

ascii_code = random.randint(65, 90)

print(chr(ascii_code))