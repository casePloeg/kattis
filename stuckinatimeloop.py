import sys


# get the number of times the magic word must be said
n = int(sys.stdin.readline())

# say the magic word n amount of times given <n>
for i in range(1, n+1):
    print(str(i) + ' Abracadabra')