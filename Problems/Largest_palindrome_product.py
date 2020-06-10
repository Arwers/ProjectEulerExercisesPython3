# Exercise 4: Largest palindrome Product

# At the beginning, we need to make function that will check is our number a palindrome
def is_palindrome(number):
    # number1 = list for elements of the number
    number1 = []
    # palnum = variable for our palindrome
    palnum = ''
    # Now we split our number to elements(ex. number = 909, number1 = [9, 0, 1])
    for i in number:
        number1.append(i)
    # Now we need to reverse the number, so we are adding elements to front of palnum
    for j in number1:
        palnum = j + palnum
    # If number is palindrome, it means that it needs to be equal to palnum
    if number == "".join(palnum):
        return True

    else:
        return False


# We will look for the biggest palindrome, so we make variable for it
biggest_pal = 0
# We need a number between 999 and 100, bcs it needs to have three digits
for i in range(999, 99, -1):
    # We need a number between 999 and 100, bcs it needs to have three digits(same situation)
    for j in range(999, 99, -1):
        # We multiplicate numbers i and j
        multi = j * i
        # We need to check if multi is a palindrome or not
        if is_palindrome(str(multi)) is True:
            # If it is and it's bigger than our temporary biggest palindrome, we overwrite biggest_pal
            if biggest_pal < multi:
                biggest_pal = multi

# At the end we just need to check what our biggest palindrome looks like
print(biggest_pal)
