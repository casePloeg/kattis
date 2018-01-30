import sys


# get the number of matches, and dimensions of the box
info = sys.stdin.readline()
# split the information into a list
info = info.split()
# create a variable for the number of matches
n = int(info[0])
# create a tuple for the dimensions of the box
w = int(info[1])
h = int(info[2])
# calculate the greatest length that will fit in the box
# this will be the hypotenuese formed by the width and height
max_length = (w**2 + h**2)**(1/2)
# iterate through all the matches
for i in range(0, n):
    # get the current match length
    match = int(sys.stdin.readline())
    # if the length is <= the max length then the match fits
    if(match <= max_length):
        msg = 'DA'
    # else , the match does not fit
    else:
        msg = 'NE'
    # output whether the box fits or not
    print(msg)