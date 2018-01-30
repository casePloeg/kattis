import sys


# get the number of cups
n = int(sys.stdin.readline())
# create a dictionary that maps size to colour
size_to_colour = {}
# iterate through the cups
for i in range(0, n):
    # read the cup information split into a list
    info = sys.stdin.readline().split()
    
    # if the cup has a digit as the first letter then it is radius first
    if(info[0][0].isdigit()):
        # map the cup's given radius to it's colour
        size = int(info[0])
        size_to_colour[size] = info[1]
    # else
    else:
        # map the cup's given radius multiplied by 2 to it's colour
        size = (int(info[1]) * 2)
        size_to_colour[size] = info[0]
# create a list containing all the keys from size to colour dictionary
size_list = list(size_to_colour.keys())
# sort the list to smallest to largest
size_list.sort()
# iterate through the list that contains the size of the cups
for i in range(0, len(size_list)):
    # output the colour that is mapped to the current size
    colour = size_to_colour[size_list[i]]
    print(colour)
