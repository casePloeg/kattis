import math


n = int(input())
while n != 0:
    dests = []
    x_total = 0
    y_total = 0
    for i in range(n):
        dirs = input().split()
        x = float(dirs.pop(0))
        y = float(dirs.pop(0))
        angle = 0
        for j in range(0, len(dirs), 2):
            action = dirs[j]
            val = float(dirs[j+1])
            if action == 'start':
                angle += val
                angle %= 360
            elif action == 'walk':
                y += math.sin(math.radians(angle)) * val
                x += math.cos(math.radians(angle)) * val
            elif action == 'turn':
                angle += val
                angle %= 360
        dests.append((x,y))
        x_total += x
        y_total += y
    x_avg, y_avg = x_total / n, y_total / n
    d = 0
    for dest in dests:
        x, y  = dest
        d = max(math.hypot(x-x_avg, y-y_avg), d)
    print(x_avg, y_avg, d)
    n = int(input())
    


