import math 


def inside_circle(x1, y1, x2, y2, rsq):
    dx = x1 - x2
    dy = y1 - y2
    dist = dx * dx + dy * dy 
    return dist <= rsq


c = int(input())
for _ in range(c):
    n = int(input())
    circles = []
    for i in range(n):
        x, y, v, color = input().split()
        x, y, v = map(float, (x,y,v))
        rsq = (v / math.pi)
        circles.append((x, y, rsq, color))
    circles = circles[::-1]
    
    m = int(input())
    for i in range(m):
        i, j = map(float, input().split())
        for x, y, rsq, color in circles:
            if inside_circle(x, y, i, j, rsq):
                print(color)
                break
        else:
            print('white')

        
