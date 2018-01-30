import sys


# get the number of iterations
i = int(sys.stdin.readline())

# init the starting points
start = 2
score = start**2
# iterate through the number of iterations
for j in range(0, i):
    # the points at top of the square are equal to the points before the
    # iteration plus that amount minus 1. This is because there is 1 middle
    # point for every 2 original points
    start = start + (start - 1)
    
score = start**2
# output the score 
print(score)