n, b = map(int, input().split())
if sum(map(lambda x: 2**x, range(0, b+1))) < n:
    print('no')
else:
    print('yes')
