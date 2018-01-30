import sys


# get the matrix info
info = sys.stdin.readline().split()
# convert elements to ints
for i in range(0, len(info)):
    info[i] = int(info[i])
# create variables for the info
r = info[0]
c = info[1]
z_r = info[2]
z_c = info[3]
# create a list that will hold the matrix
matrix_list = []
# iterate through the rows of the given matrix
for i in range(0, r):
    # read the line
    row = sys.stdin.readline().replace('\n','')
    matrix_list.append([])
    # iterate through the colomns of the given matrix
    for j in range(0, c):
        # save to current character to the list
        matrix_list[i].append(row[j])
# cut the first element of each row
# perform the transformations
# create a list for the transformed matrix
stretched_matrix = []
# loop through the rows
for i in range(0, r):
    # loop through the colomuns
    stretched_matrix.append([])
    for j in range(0, (c)):
        # repeat each element z_r times
        for k in range(0, z_c):
            stretched_matrix[i].append(matrix_list[i][j % c]) 

# loop through the rows
for i in range(0, r):
    # convert the row into a string
    row_string = ''
    for j in range(0, (z_c * c)):
        row_string = row_string + stretched_matrix[i][j]
    # output the row r_c times
    for j in range(0, z_r):
        print(row_string)