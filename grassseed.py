import sys


# get the cost of seed to sow 1 m^2
c = float(sys.stdin.readline())
# get the number of laws to sow
l = int(sys.stdin.readline())
# create a variable for the total cost
total_cost = 0
# iterate through the lawns
for i in range(0, l):
    # get the info about the laws
    lawn_info = sys.stdin.readline().split()
    # convert the elements to floats
    for j in range(0, len(lawn_info)):
        lawn_info[j] = float(lawn_info[j])
    # create variables for the width and height
    w = lawn_info[0]
    h = lawn_info[1]
    # calculate the cost for the current lawn
    curr_cost = (w*h) * c
    # increment the total cost with the current cost
    total_cost += curr_cost
# output the total cost
print(total_cost)