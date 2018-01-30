import sys

# get the number of test cases
n = int(sys.stdin.readline())
# iterate through the test cases
for i in range(0, n):
    # get the test case
    test = sys.stdin.readline().replace('\n','')
    # if it is an addition problem
    if(test[0].isdigit()):
        # find where the + sign is
        plus = test.find('+')
        # create variable for first number
        num1 = int(test[:plus])
        # create variable for the second number
        num2 = int(test[plus+1:])
        # sum the numbers
        num_sum = num1 + num2
        # output the answer
        print(num_sum)
    # if it is 'P=NP'
    else:
        # output 'skipped'
        print('skipped')