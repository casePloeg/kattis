import math


a, b, h = map(int, input().split())
if a >= h:
    print(1)
else:
    print(math.ceil((h-a) / (a-b)) + 1)
