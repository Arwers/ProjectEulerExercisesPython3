# Exercise 1: Multiples of 3 and 5

# multiples variable is sum of multiples of 3 and 5
multiples = 0

# we need to find multiples BELOW 1000, so we use loop for that
for i in range(1000):
    # when i % 3 == 0, then add i to multiples
    if i % 3 == 0:
        multiples += i
        # we use "continue" at the end because some of multiples of 5 are also multiples of 3
        continue
    # when i % 5 == 0, then add i to multiples
    elif i % 5 == 0:
        multiples += i

print(multiples)
