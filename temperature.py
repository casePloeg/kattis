x, y = map(int, input().split())
if y == 1 and x == 0:
    print('ALL GOOD')
elif y == 1 and x != 0:
    print('IMPOSSIBLE')
else:
    print(x / (1-y))

