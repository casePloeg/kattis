import math


d, n = map(float, input().split())
n = int(n)
while n != 0:
    hives = [list(map(float, input().split())) for _ in range(n)]
    count = 0
    for h1 in hives:
        sour = False
        for h2 in hives:
            if h1 != h2:
                x1, y1 = h1
                x2, y2 = h2
                dist = math.hypot(x1-x2, y1-y2) 
                if dist <= d:
                    sour = True
                    break
        else:
            count += 1
    print(str(n-count), 'sour,', str(count), 'sweet')
    d, n = map(float, input().split())
    n = int(n)

