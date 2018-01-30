import sys


# get the information for the question
info = sys.stdin.readline().split()
# convert elements to integers
for i in range(0, len(info)):
    info[i] = int(info[i])
# maximimum dimensions will be the smallest length x the second largest length
info.sort()
max_area = info[0] * info[2]
print(max_area)