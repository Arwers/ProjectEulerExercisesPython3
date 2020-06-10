# Exercise 4: Largest palindrome Product


def is_palindrome(number):

        number1 = []
        palnum = ''

        for i in number:
            number1.append(i)

        for j in number1:
            palnum = j + palnum

        if number == "".join(palnum):
            return True

        else:
            return False


biggest_num = 0
for i in range(999, 99, -1):

    for j in range(999, 99, -1):
        mnozenie = j * i

        if is_palindrome(str(mnozenie)) is True:

            if biggest_num < mnozenie:
                biggest_num = mnozenie

print(biggest_num)
