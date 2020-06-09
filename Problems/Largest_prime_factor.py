# Exercise 3: Largest prime factor

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


# Now we need to make function that will find largest prime factor
def largest_factor(number):
    # Google: You can get the largest factor (other than itself) by dividing it by the smallest prime factor.
    # In this example, we will divide by numbers above 2(not only primes) and then check if it's prime.
    counter = 2
    while counter < number:
        # If number % counter == 0, then we will know that it divides without remainder(Possible LPF)
        if number % counter == 0:
            number = number/counter
            number = int(number)
        # Now we check if number is prime - if it is, then we will have our LPF
        if is_prime(number) is True:
            break
        # if it isn't, we add 1 to counter and try again
        else:
            counter += 1

    return number


print(largest_factor(600851475143))
