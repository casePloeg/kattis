import sys


# get the info split into a list
info = sys.stdin.readline().split()
# covert elements to integers
for i in range(0, len(info)):
    info[i] = int(info[i])

# create a variable for left
l = info[0]
# create a variable for right
r = info[1]
# if the moose has no tines its not a moose fam
if(l == r and l == 0):
    print('Not a moose')
else:
    
    # if left is the same as right, the moose is even
    if(l == r):
        type = 'Even'
        # number of tines is equal to the right
        tines = r
        # if they are different the moose is odd
    else:
        type = 'Odd'
        # number of tines is equal to the largest of left and right
        if(l > r):
            tines = l
        else:
            tines = r
    # output even/odd and number of tines
    print(type + ' ' + str(tines * 2))