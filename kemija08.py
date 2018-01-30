import sys


# get the line that needs to be decoded
line = sys.stdin.readline().replace('\n','')
# create a variable for the decoded line
decoded = ''

vowels = {'a', 'e', 'i', 'o', 'u'}
# iterate through the line that needs to be decoded
i = 0
while(i < len(line)):
    # add the current char to the decoded line
    decoded = decoded + line[i]
    # if the current character is in {'a', 'e', 'i', 'o', 'u'}
    if(line[i] in vowels):
        # step ahead by 2
        i += 2
    i += 1
# output the decoded line
print(decoded)
