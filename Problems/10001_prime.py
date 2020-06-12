# Exercise 7: 10001 prime

# First, we need to make function that will help us check if number is prime
def is_prime(number):
    int(number)
    prime = True  # True = prime, False = not prime

    # All of numbers below and equal to 1 are not prime
    if number <= 1:
        return False

    else:
        # Prime number is a number, that divides (without a remainder) only by 1 and by itself
        for j in range(2, number):
            # If number % j is equal to 0, then number have other dividers and isn't prime
            if number % j == 0:
                return False
    # if number passed the loop, then it is prime
        if prime is True:
            return True


counter = 0  # It will count how many primes we had
number = 1  # It's current number
while True:
    boolean = is_prime(number)  # Check if number is prime

    if boolean is True:  # if it is, add 1 to counter
        counter += 1

    if counter == 10001:  # Check if counter == 10001, if it is - print current number
        print(number)
        break

    number += 1  # Make current number bigger by one and check again
