import sys


# get the numbers
numbers = sys.stdin.readline().split()
# get the order of the numbers
order = sys.stdin.readline().replace('\n','')
# create a dictionary that maps a letter ( A, B, or C) to a value, such that
# the number that maps to A is less than B which is less than C
# determine the lowest number
lowest = 100
for i in range(0, 3):
    if(int(numbers[i]) < lowest):
        lowest = int(numbers[i])
# determine the second lowest and highest number
del numbers[numbers.index(str(lowest))]
if(int(numbers[0]) <= int(numbers[1])):
    second = int(numbers[0])
    highest = int(numbers[1])
else:
    second = int(numbers[1])
    highest = int(numbers[0])
letter_to_value = {'A': str(lowest), 'B': str(second), 'C': str(highest)}
# iterate through the given order
msg = ''
for i in range(0, len(order)):
    msg = msg + letter_to_value[order[i]] + ' '
msg = msg.strip()
print(msg)