import math


m = int(input())
for _ in range(m):
    x, y = map(float, input().split())
    n = int(input())
    candles = [list(map(float, input().split())) for i in range(n)]
    flag = False
    for c in candles:
        x2, y2 = c
        if math.hypot(x-x2, y-y2) <= 8:
            print('light a candle')
            flag = True
            break
    if not flag:
        print('curse the darkness')
