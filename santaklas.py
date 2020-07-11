import math


h, v = map(int, input().split())
a = 0
if 0 <= v <= 180:
    print('safe')
else:
    if v < 270:
        a = 90 - (v % 90)
    else:
        a = v % 90

    dist = h / math.cos(math.radians(a))
    print(math.floor(dist))

