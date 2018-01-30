import sys


# get the input 
line = sys.stdin.readline()

# split the input into a list
line_list = line.split()

# create a set that has all the elements of the list
line_set = set(line_list)

# if the set and list have the same length then there are no duplicates within
# the set
if(len(line_list) == len(line_set)):
    # output yes, as no words are repeated
    print('yes')
# if the lengths are not the same something is being repeated
else:
    # output no
    print('no')
