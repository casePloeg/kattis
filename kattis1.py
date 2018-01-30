import sys
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
# get the number of lines
n = int(sys.stdin.readline())
# loop through the lines
for i in range(0, n):
    line = sys.stdin.readline()
    # create a copy of the alphabet
    alpha_copy = ALPHA[:]
    # convert the characters of the input to lower case
    line = line.lower()
    # loop through the characters
    for char in line:
        # if the character is in the alphabet copy
        if(char in alpha_copy):
            # take the character out of the copy
            alpha_copy = alpha_copy.replace(char, '')
    
    # if the alphabet copy is empty
    if(len(alpha_copy) == 0):
        # the output will be pangram
        output = 'pangram'
    else:
        # the output will be the remaining characters from the alphabet
        output = 'missing ' + alpha_copy
    
    # print the output
    print(output)
