import math


a, b, s, m, n = map(int, input().split())
while a + b + s + m + n != 0:
    x = a * m
    y = b * n
    h = math.hypot(y, x)
    A = math.degrees(math.atan2(y, x))
    V = h / s
    print('{:.2f} {:.2f}'.format(A, V))
    a, b, s, m, n = map(int, input().split())

