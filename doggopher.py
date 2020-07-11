import sys
import math

gx, gy, dx, dy = map(float, input().split())
holes = []
for line in sys.stdin:
    holes.append(list(map(float, line.split())))

flag = False
for h in holes:
    x, y = h
    if math.hypot(dx-x, dy-y) / 2 >= math.hypot(gx-x, gy-y):
        print('The gopher can escape through the hole at (' + '{:0.3f}'.format(x) + ',' + '{:0.3f}'.format(y) + ').')
        flag = True
        break
if not flag:
    print('The gopher cannot escape.')
