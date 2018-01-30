import sys


# get the spam line
line = sys.stdin.readline().replace('\n','')
# create counters for whitespace, lowercase, uppercase, and symbols
white = 0
lower = 0
upper = 0
symbo = 0
# iterate through the line
for char in line:
    # if the current character is an underscore increment the whitespace
    # counter
    if(char == '_'):
        white += 1
    # if the current character is a letter and is lower case increment the
    # lowercase counter
    elif(char.islower()):
        lower += 1
    # if the current character is a letter and is uppercase increment the
    # uppercase counter
    elif(char.isupper()):
        upper += 1
    # else increment the symbol counter
    else:
        symbo += 1
# calculate the percentage of whitespace, lower, upper, symbol, relative to
# the total amount of characters
total_char = len(line)
white_per = white / total_char
lower_per = lower / total_char
upper_per = upper / total_char
symbo_per = symbo / total_char
# output the percentage of whitespace, lower, upper, symbol
print(white_per)
print(lower_per)
print(upper_per)
print(symbo_per)