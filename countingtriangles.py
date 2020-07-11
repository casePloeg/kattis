EPS = 10 ** (-9)
# given two points on a line return the params a,b,c
# representing the line such that ax + by + c = 0
def pointsToLine(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    la, lb, lc = 0, 0, 0
    if abs(x1 - x2) < EPS:
        # avoiding division by zero in the case of vertical
        # lines
        la = 1.0
        lb = 0.0
        lc = -x1
    else:
        la = -(y1 - y2) / (x1 - x2)
        lb = 1.0
        lc = -(la * x1) - y1
    return (la, lb, lc)

# two lines are parralel if both a and b coefficients are
# the same
def parrallel(l1, l2):
    l1a, l1b, l1c = l1
    l2a, l2b, l2c = l2
    return abs(l1a - l2a) < EPS and abs(l1b - l2b) < EPS


def intersect(l1, l2):
    l1a, l1b, l1c = l1
    l2a, l2b, l2c = l2
    if parrallel(l1, l2):
        return False, (0, 0)
    px = (l2b * l1c - l1b * l2c) / (l2a * l1b - l1a * l2b)
    # special case, vertical lines
    if abs(l1b) > EPS:
        py = -(l1a * px + l1c)
    else:
        py = -(l2a * px + l2c)
    return True, (px, py)


def withinBounds(ip, p1, p2, p3, p4):
    xi, yi = ip
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3
    if y1 > y2:
        y1, y2 = y2, y1
    if y3 > y4:
        y3, y4 = y4, y3
    return (x1 <= xi <= x2) and (x3 <= xi <= x4) and (y1 <= yi <= y2) and (y3 <= yi <= y4)

def triangle(p1, p2, p3, p4, p5, p6):
    l1 = pointsToLine(p1, p2)
    l2 = pointsToLine(p3, p4)
    l3 = pointsToLine(p5, p6)
    i1, ip1 = intersect(l1, l2)
    if i1:
        i2, ip2 = intersect(l2, l3)
        if i2:
            i3, ip3 = intersect(l1, l3)
            if i3:
                if i1 and i2 and i3 and withinBounds(ip1, p1, p2, p3, p4) and withinBounds(ip2, p3, p4, p5, p6) and withinBounds(ip3, p1, p2, p5, p6):
                    return True
    return False



n = int(input())
while n != 0:
    lines = [list(map(float, input().split())) for x in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1, x2, y2 = lines[i]
                x3, y3, x4, y4 = lines[j]
                x5, y5, x6, y6 = lines[k]
                p1 = (x1, y1)
                p2 = (x2, y2)
                p3 = (x3, y3)
                p4 = (x4, y4)
                p5 = (x5, y5)
                p6 = (x6, y6)
                if triangle(p1, p2, p3, p4, p5, p6):
                    count += 1
    print(count)
    n = int(input())
    
    

