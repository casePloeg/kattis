import sys

# get the number of test cases
n = int(sys.stdin.readline())

# iterate through the test cases
for i in range(0, n):
    # create variables for the two strings that need to be compared
    str1 = sys.stdin.readline().replace('\n','')
    str2 = sys.stdin.readline().replace('\n','')
    # create a variable for the similarites of the two strings
    similiar = ''
    # iterate through one of the strings
    for j in range(0, len(str1)):
        # if the strings are equivalent for the current index represent it with
        # a '.'
        if(str1[j] == str2[j]):
            similiar = similiar + '.'
        # differences are represented with a '*'
        else:
            similiar = similiar + '*'
    # output the two strings and then the similiarities and a blank line
    print(str1)
    print(str2)
    print(similiar + '\n')