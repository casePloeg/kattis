import sys
import math

# D(t_1, t_2) = |x_1 - x_2| + |y_1 - y_2|
# get the radius
r = int(sys.stdin.readline())
# calculate euclidian area
area1 = math.pi * (r)**2
# calculate taxicab area
area2 = 2 * (r)**2
print(area1)
print(area2)