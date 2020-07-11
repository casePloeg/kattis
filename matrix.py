import sys

n = 1
for line in sys.stdin:
    a, b = map(int, line.split())
    c, d = map(int, input().split())
    det = (a*d) - (b*c)
    a, b, c, d = a//det, b//det, c//det, d//det

    print('Case ', n, ':', sep='')
    print(d, -b)
    print(-c, a)
    n += 1
    input()
