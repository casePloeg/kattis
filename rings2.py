import sys 
import math

# get the dimensions
dim = sys.stdin.readline().split()
# convert the elements to integers
rows = int(dim[0])
cols = int(dim[1])
# create a list for the tree input
tree_list = []
for i in range(0, rows):
    row = sys.stdin.readline().split()
    tree_list.append([])
    for j in range(0, cols):
        tree_list[i].append(row[j])

# create a variable for the amount of rings that need to be iterated through
rings = int(math.ceil((rows / 2)))
# iterate through the rings of the tree
