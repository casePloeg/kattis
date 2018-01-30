import sys


# get the number of test cases
t = int(sys.stdin.readline())

# iterate through the test cases
for i in range(0, t):
    print('Test ' + str(i + 1))
    # get the number of rows and colomns
    info = sys.stdin.readline().split()
    r = int(info[0])
    c = int(info[1])
    # create a list for the matrix
    matrix = []
    # iterate through the matrix
    for j in range(0, r):
        # read the row
        row = sys.stdin.readline().replace('\n','')
        matrix.append([])
        for k in range(0, c):
            matrix[j].append(row[k])
    # iterate through the rows in reverse order
    for j in range(r-1, -1, -1):
        reversed_row = matrix[j][::-1]
        row = ''
        # iterate through the reversed row
        for k in range(0, c):
            row = row + reversed_row[k]
        # output the row reversed
        print(row)
  
            