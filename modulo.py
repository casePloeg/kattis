import sys

# create a set for the remainders
remainder_set = set()

# iterate through the input lines
for line in sys.stdin:
    # convert the line to an integer
    num = int(line)
    # calculate the current number modulo 42
    remainder = num % 42
    # add the remainder to the set
    remainder_set.add(remainder)

# calculate the length of the remainder set (number of remainders)
num_remainders = len(remainder_set)

# output the number of remainders
print(num_remainders)