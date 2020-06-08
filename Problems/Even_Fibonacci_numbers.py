# Exercise 2: Even Fibonacci numbers

# fibosum variable represent sum of even Fibonacci numbers
fibosum = 0

# a, b, c are first, second and third digits of Fibonacci sequence
a = 0
b = 1
c = 1

# We know that the Fibonacci sequence values do not exceed four million (from task)
while c <= 4000000:
    # formula for Fibonacci sequence
    c = a + b
    a = b
    b = c
    # Number needs to be even, so we check it using c % 2
    if c % 2 == 0:
        # if it is, we simply add c to the fibosum
        fibosum += c

print(fibosum)
