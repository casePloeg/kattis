import sys 



# get the number of stars the flag has
s = int(sys.stdin.readline())

# output the number of stars
print(str(s) + ':')

# calculate the maximum amount x
if(s % 2 == 0):
    max_x = s//2
else:
    max_x = s//2 + 1

# iterate through x and y, ensuring that x >= y and x is only ever greater by 1
for x in range(2, (max_x + 1)):
    y = x - 1
    # create a variable that will hold the sum of x and y
    sum = 0
    # create a variable to keep track of whether x or y needs to be added next
    x_turn = True
    # iterate through adding x and y until the sum is >= the number of stars
    while(sum < s):
        if(x_turn):
            sum += x
            x_turn = False
        else:
            sum += y
            x_turn = True
        # if the sum equals the number of stars
        if(sum == s):
            # output the combination
            print(str(x) + ',' + str(y))
    sum = 0
    # iterate through adding x and y until the sum is >= the number of stars
    while(sum < s):
        sum += x

        # if the sum equals the number of stars
        if(sum == s):
            # output the combination
            print(str(x) + ',' + str(x))  
    