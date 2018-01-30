import sys


# get the number that needs to be reversed
n = int(sys.stdin.readline())

# covert the number to binary

# find the greatest power of 2 the number is bigger than
# create a variable that represents whether the number is
# still bigger than the current power or not
is_bigger = True
# create a variable to represent the current power
power = 0
# iterate until the highest power is found
while(is_bigger):
    # if the biggest power is found stop the loop
    if(n <= 2**power):
        is_bigger = False
    else:
        power += 1

# create a number to represent the binary number
binary = 0
# iterate through the powers, starting at biggest
for i in range(power, -1, -1):
    # determine whether 2 to the current power is within the number
    add_1 = ((n - 2**i) >= 0)
    # if a 1 can be added
    if(add_1):
        # reduce the number
        n = n - 2**i
        # increment the binary number
        binary += 10 ** i

# conver the binary number to a string and then reverse it
binary = str(binary)
binary = binary[::-1]
# create a variable for the reversed number
reversed_num = 0
# create a variable for the power
power = 0
# find the number that corresponds to the binary number
for i in range(len(binary)-1, -1, -1 ):
    if(binary[i] == '1'):
        reversed_num += 2 ** power
    power += 1

# output the reversed number
print(reversed_num)
    