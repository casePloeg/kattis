import sys


# get the word the will be transformed
word = sys.stdin.readline().replace('\n','')

# create a variable to keep track of the number of days needed
days = 0
# iterate through every third word
for i in range(0, len(word)):
    # if the first word of the 3 letter sequence is not an 'P'
    if((i % 3 == 0) and (word[i] != 'P')):
        # increment the day counter by 1
        days += 1
    # if the second word of the 3 letter sequence is not an 'E'
    elif((i % 3 == 1) and (word[i] != 'E')):
        # increment the counter by 1
        days += 1
    # if the third word of the 3 letter sequence is not an 'R'
    elif((i % 3 == 2) and (word[i] != 'R')):
        # increment the counter by 1
        days += 1

# output the number of days needed
print(days)