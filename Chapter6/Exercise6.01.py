def get_pentagonal_number(n):
    number = n * (3 * n - 1) / 2
    return int(number)

def main():
    count = 1
    for i in range(1, 101):
        print(get_pentagonal_number(i), end=' ')
        if count % 10 == 0:
            print()
            count = 0

        count += 1

main()
