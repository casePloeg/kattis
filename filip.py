import sys


# get the two numbers as a list
numbers = sys.stdin.readline().split()

# flip each number and convert to int
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i][::-1])
# output the biggest number
if(numbers[0] > numbers[1]):
    biggest = numbers[0]
else:
    biggest = numbers[1]
print(biggest)
