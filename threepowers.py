n = int(input())
# lg(10^20) gives us an upper bound on number of digits
# in our bitmask
threes = list(map(lambda x: 3 ** x, range(70)))
while n !=0:
    n -= 1
    s = []
    for i in range(70):
        if (n & (1<<i)):
            s.append(threes[i])
    print('{ ', ', '.join([str(x) for x in s]), ' }', sep='')
    n = int(input())

