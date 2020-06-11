# Exercise 6: Sum square difference

square = 0  # We will add here our n^m numbers
sum = 0  # We will add here all the numbers to make them later a square
for i in range(101):  # We need first 100 numbers, but range() skips the last digit, so num is 101 not 100
    square += i * i
    sum += i

#  Now make square of our sum
sum = sum*sum
print(sum - square)  # Print the answer
