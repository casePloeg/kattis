import sys
import math

# x(t) = vtcos(theta)
# y(t) = vtsin(theta) - (1/2)gt^2
# g = 9.81 m/s^2


# get the number of test cases
n = int(sys.stdin.readline())

# iterate through the test cases
for i in range(0, n):
    # get the data given as a list
    info = sys.stdin.readline().split()
    # convert elements to floats
    for j in range(0, len(info)):
        info[j] = float(info[j])
    # create a variables for the appropriate data
    v = info[0]
    theta = math.radians(info[1])
    x_1 = info[2]
    h_1 = info[3]
    h_2 = info[4]
    # create constant g for gravity
    g = 9.81
    # solve for t using x(t)
    t = (x_1) / (v * math.cos(theta))
    # solve for y using y(t)
    y = (v * t * math.sin(theta)) - ((1 / 2) * g * t**2)
    # if the calculated y is within the boundaries, the shot is safe
    if((y > (h_1 + 1)) and (y < (h_2 - 1))):
        msg = 'Safe'
    # else, the shot is not safe
    else:
        msg = 'Not Safe'
    # output whether the shot is safe or not
    print(msg)