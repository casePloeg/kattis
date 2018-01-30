import sys
import math

# get the info
info = sys.stdin.readline().split()
# convert elements to ints
for i in range(0, len(info)):
    info[i] = int(info[i])
# calculate area of pizza with cheese
c_area = math.pi * (info[0] - info[1])**2
# calculate the total area of the pizza
t_area = math.pi * (info[0])**2
# calculate the percentage with cheese
c_percent = (c_area / t_area) * 100
# output the percentage
print(c_percent)