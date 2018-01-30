import sys 


def sum_digits(num):
    '''(int) -> int
    Given an integer, return the sum of the integer's digits
    REQ: num >= 0

    >>> sum_digits(11)
    2
    >>> sum_digits(0)
    0
    '''
    # determine the highest power of 10 that the given number is bigger than
    is_bigger = True
    power = 0
    while(is_bigger):
        if(not(num > 10**power)):
            is_bigger = False
        else:
            power += 1
    # starting at the calculated power of ten, calculate the sum of digits by
    # iterating through the powers of 10 until 0
    # create a variable for the sum of digits
    sum_dig = 0
    for i in range(power-1, -1, -1):
        current_dig = (num // 10**i)
        num = (num - ((current_dig) * (10**i)))
        sum_dig += current_dig
    # return the calculated sum of digits
    return sum_dig

# read the first line as an integer
num = int(sys.stdin.readline())
# iterate through the test until 0 is found
while(num != 0):
    # create a variable that will represent the number that the current test
    # case will be multiplied by. This number will start at 11, as it must be
    # greater than 10
    multi = 11
    # create a variable for the sum of the digits of the test case
    sum_dig = sum_digits(num)
    # create a variable for the sum of the digits of the test case multiplied
    # by the number
    multi_sum_dig = sum_digits((multi * num))
    # iterate until a number is found that when the test case is multiplied by
    # the number the sum of digits is the same
    while(sum_dig != multi_sum_dig):
        multi += 1
        multi_sum_dig = sum_digits((multi * num))
    # output the number
    print(multi)
    # read next line as an integer
    num = int(sys.stdin.readline())
