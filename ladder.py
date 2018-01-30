import sys
import math


# get the info as a list
info = sys.stdin.readline().split()

# convert elements to integers
for i in range(0, len(info)):
    info[i] = int(info[i])

# make variables for height and degrees
h = info[0]
v = info[1]
# convert the degrees to radians
v = math.radians(v)

# hyp = (height / sin(v))
hyp = h / math.sin(v)
# round up to nearest integer
hyp = math.ceil(hyp)

# output the length of the ladder
print(str(hyp))