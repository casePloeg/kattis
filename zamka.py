import sys


# get the first integer
l = int(sys.stdin.readline())
# get the second integer
d = int(sys.stdin.readline())
# get the third integer
x = int(sys.stdin.readline())

# calculate n
# iterate starting at l to d while n has not been found
i = l
found_n = False
while((i < (d+1)) and (not found_n)):
    # if the sum of the digits of the current number is equivalent to x then n
    # has been found
    # convert the current number to a string
    num = str(i)
    # create a list for the digits
    dig_list = []
    # loop through the digits and sum them
    for dig in num:
        dig_list.append(int(dig))
    dig_sum = sum(dig_list)
    # if n is found stop the loop
    if(dig_sum == x):
        n = i
        found_n = True
    # increment i 
    i += 1
# calcluate m
# iterate starting at d to l while m has not been found
j = d
found_m = False
while((j > (l-1)) and (not found_m)):
    # if the sum of the digits of the current number is equivalent to x then n
    # has been found
    # convert the current number to a string
    num = str(j)
    # create a list for the digits
    dig_list = []
    # loop through the digits and sum them
    for dig in num:
        dig_list.append(int(dig))
    dig_sum = sum(dig_list)
    # if n is found stop the loop
    if(dig_sum == x):
        m = j
        found_m = True
    # increment j by 1
    j -= 1
# output n and the m
print(n)
print(m)