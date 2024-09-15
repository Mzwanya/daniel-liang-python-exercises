NUMBER_OF_PRIMES_PER_LINE = 8 # Display 10 per line
count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness
while number <= 1000:
    is_prime = True

    # A loop to find prime numbers from 2, 3, 5...
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    # Display the prime number and increase the count
    if is_prime:
        count += 1
        # Display the number and advance to the new line
        print(format(number, "5d"), end = ' ')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print() # Jump to the new line

    number += 1
