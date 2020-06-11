# Exercise 5: smallest multiple (definitely not the best way to do it)

number = 1  # Variable containing number checking at the moment
while True:

    remainder = False  # False = no remainder, true = have remainder
    for i in range(1, 21):  # From the task we know that number needs to be evenly divisible in range 1-20

        if number % i != 0:  # if divided number have remainder, change the value of remainder var
            remainder = True
            break  # If it have remainder, there's no sense of checking further

    if remainder is False:  # Here we check if number meets our requirements
        print(number)  # If it is, we print the number and break while() loop
        break

    else:  # If no, we are making our num bigger bigger by one and try again
        number = number + 1

# PS. The method is probably easiest, but it takes a while to give the result
