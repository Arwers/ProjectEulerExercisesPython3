# Exercise 3: Largest prime factor


def is_prime(number1):
    int(number1)
    prime = True

    if number1 <= 1:
        return False

    else:

        for j in range(2, number1):

            if number1 % j == 0:
                return False

        if prime is True:
            return True


def largest_factor(number):
    counter = 2.0
    while counter < number:

        if number % counter == 0:
            number = number/counter
            number = int(number)

        if is_prime(number) is True:
            break

        else:
            counter += 1

    return number


print(largest_factor(600851475143))
