import math



# usually pass in points so that polygon has first coord
# as first and last index, modified this one bc first coord
# is only at first element (use modulus)
def area(points):
    res = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%len(points)]
        res += (x1 * y2 - x2 * y1)
    return abs(res) / 2

n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]
# translate so nothing is negative (move min x, y to (0, 0))
min_x = min(map(lambda x: x[0], points))
min_y = min(map(lambda x: x[1], points))
for p in points:
    p[0] -= min_x
    p[1] -= min_y

x = int(input())
a = area(points)
print(a)
ratio = math.sqrt(x/a)
for i in range(n):
    points[i][0] *= ratio
    points[i][1] *= ratio
for p in points:
    print(' '.join([str(x) for x in p]))
