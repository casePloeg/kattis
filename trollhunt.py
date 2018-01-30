import sys


# get the info as a list
info = sys.stdin.readline().split()
# converts the elements to integers
for i in range(0, len(info)):
    info[i] = int(info[i])

# create variables for # of bridges, # of knights, and # of knights per group
b = info[0] - 1
k = info[1]
g = info[2]
# calculate the number of groups the knights will make
num_groups = k // g
# calculate the number of days before the troll is caught
if(b % num_groups == 0):
    days = b // num_groups
else:
    days = b // num_groups + 1
# output the number of days before the troll is caught
print(str(days))