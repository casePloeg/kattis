import sys


# get the word
word = sys.stdin.readline()

# if there is 'ss' within the word it is a hiss
if(word.find('ss') != -1):
    msg = 'hiss'
# else, no hiss
else:
    msg = 'no hiss'

# output the result
print(msg)