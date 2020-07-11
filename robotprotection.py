import math
import functools


# area of a convex hull, using Graham Scan, runs in O(nlogn:w)

def area(points):
    # returns area which is half the determinant of the points
    # matrix
    res = 0
    x1, x2, y1, y2 = 0, 0, 0, 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        res += (x1 * y2 - x2 * y1)
    return abs(res) / 2

def dist(a, b):
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(a, b)))

def toVec(a, b):
    ax, ay = a
    bx, by = b
    return (bx - ax, by-ay)

def cross(a, b):
    ax, ay = a
    bx, by = b
    return (ax * by - ay * bx)


# returns true if r is on the left side of the line pq
def ccw(p, q, r):
    return cross(toVec(p, q), toVec(p,r)) > 0


def collinear(pivot, a, b):
    ax, ay = a
    bx, by = b
    px, py = pivot
    s1 = (ay - py) * (px - bx) 
    s2 = (py - by) * (ax - px)    
    return s1 == s2 
    

def angleCmp(a, b):
    if collinear(pivot, a, b):
        if dist(pivot, a) < dist(pivot, b):
            return -1
        else:
            return 1
    ax, ay = a
    bx, by = b
    px, py = pivot
    d1x = ax - px
    d1y = ay - py
    d2x = bx - px
    d2y = by - py
    if (math.atan2(d1y, d1x) - math.atan2(d2y, d2x)) < 0:
        return -1
    else:
        return 1


pivot = (0,0)
n = int(input())
while n != 0:
    points = [tuple(map(int, input().split())) for _ in range(n)]
    # there is no area of a point or a line 
    if n <= 2:
        print(0)
    elif n == 3:
        print(area(points + [points[0]]))
    else:
        # sort by angle
        # find point with lowest Y and if tie, rightmost X
        p0 = 0
        for i in range(n):
            x1, y1 = points[p0]
            x2, y2 = points[i]
            if (y2 < y1) or (y2 == y1 and x2 > x1):
                p0 = i
        # swap points[0] with points[p0]
        points[p0], points[0] = points[0], points[p0]

        # sort by angle w.r.t pivot point p0
        pivot = points[0]
        points = [points[0]] + sorted(points[1:], key=functools.cmp_to_key(angleCmp))
        s = [points[-1], points[0], points[1]]
        i = 2
        while i < n:
            j = len(s) - 1
            # accept if left turn (counter clockwise)
            # points[i] is on the left hand side of 
            # the two top points on the stack
            if ccw(s[j-1], s[j], points[i]):
                s.append(points[i])
                i += 1
            else:
                # pop until we have a left turn
                s.pop()
        # resulting stack is the convex hull
        # with last and first item the same
        # last step is to print the area of the convex hul
        print(area(s))

    n = int(input())


