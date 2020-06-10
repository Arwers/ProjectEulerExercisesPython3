# Exercise 5: smallest multiple (definitely not the best way to do it)

number = 1
while True:

    remainder = False
    for i in range(1, 21):

        if number % i != 0:
            remainder = True
            break

    if remainder is False:
        print(number)
        break

    else:
        number = number + 1
