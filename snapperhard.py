t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    i = 0
    res = k % (2 ** n)
    on = res == (2 ** n) - 1 
    
    print('Case #', _+1, ': ', sep='', end='')
    if on:
        print('ON')
    else:
        print('OFF')
