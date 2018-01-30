import sys


# get the x coord
x = int(sys.stdin.readline())
# get the y coord
y = int(sys.stdin.readline())

# if x and y are positive, the point is in quadrant 1
if((x > 0) and (y > 0)):
    quadrant = 1
# elif x is positive and y is negative, the point is in quadrant 4
elif((x > 0) and (y < 0)):
    quadrant = 4
# elif x is negative and y is positive, the point is in quadrant 2
elif((x < 0) and (y > 0)):
    quadrant = 2
# else the point is in quadrant 3
else:
    quadrant = 3

# output the quadrant that the point lies in
print(quadrant)