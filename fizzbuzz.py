import sys


# get the numbers from the input
numbers = sys.stdin.readline()
# convert the line to a list
numbers = numbers.split()
# convert the elements to integers
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

# set variables for each number
n = numbers[2]
x = numbers[0]
y = numbers[1]

# iterate through the numbers 1-n
for i in range(1, (n+1)):
    # evaluate whether the current number is div by x
    div_by_x = (i % x == 0)
    # evaluate whether the current number is div by y
    div_by_y = (i % y == 0)
    # if the current number is div by x and y output FizzBuzz
    if(div_by_x and div_by_y):
        print('FizzBuzz')
    # elif the current number is div by x output Fizz
    elif(div_by_x):
        print('Fizz')
    # elif the current number is div by y output FizzBuzz
    elif(div_by_y):
        print('Buzz')
    # else (not div by x or y) output the number
    else:
        print(str(i))