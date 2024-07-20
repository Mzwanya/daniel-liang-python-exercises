'''
**5.28 (Compute e) You can approximate e by using the following series:
e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000. . ., and
100000. (Hint: Since i! = i * (i - 1) * ... * 2 * 1, then 1/i! is 1 / (i * (i - 1)!)
Initialize e and item to be 1 and keep adding a new item to e. The new item is
the previous item divided by i for i = 2, 3, 4. . . .)
'''
# TO BE CONTINUED LATER...
limit = 10000
while limit <= 100000:
    e = 1
    for i in range(1, limit + 1):
        e += (1 / e / i)
    print(f"For i = {limit}, e = {e}")
    limit += 10000
