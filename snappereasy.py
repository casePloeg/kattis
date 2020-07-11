t = int(input())
for i in range(t):
    res = ''
    n, k = map(int, input().split())
    if k % 2**n == (2**n) - 1:
        res = 'ON'
    else:
        res = 'OFF'
    print('Case #', i+1, ': ', res, sep='')
