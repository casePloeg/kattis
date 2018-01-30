import sys


# get the number of stones
n = int(sys.stdin.readline())

# if there is an even number of stones given then bob will win
if(n % 2  == 0):
    winner = 'Bob'
# if there is an odd number of stones given then alice will win
else:
    winner = 'Alice'
# output the winner
print(winner)