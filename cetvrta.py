import sys

# create a list for x coords
x_list = []
# create a list for y coords
y_list = []
# iterate through the coordinates
for line in sys.stdin:
    # split coordinates into list
    coords = line.split()
    # convert to ints
    for i in range(0, len(coords)):
        coords[i] = int(coords[i])
    # create variables for x and y
    x = coords[0]
    y = coords[1]
    # if the current x is not in the x list
    if(x in x_list):
        x_list.pop(x_list.index(x))
        # add the current x to the list
    # else
    else:
        x_list.append(x)
        # remove x from the list
    # repeat for y
    if(y in y_list):
        y_list.pop(y_list.index(y))
        # add the current x to the list
    # else
    else:
        y_list.append(y)    
# output the remaining values within the two lists
print(x_list[0], y_list[0])