import math


n = int(input())
tris = [list(map(int, input().split())) for _ in range(n)]
total = 0
for tri in tris:
    a, b, c = tri
    # c is the bottom length
    a, b = min(a, b), max(a, b)
    # using cosine law to get angles
    C = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    B = math.acos((a**2 + c**2 - b**2)/(2*a*c))
    A = math.acos((b**2 + c**2 - a**2)/(2*b*c))
    # finding length of median from point to c
    h = (1/2) * (2*(a**2+b**2)-c**2)**(1/2)
    # sin law to get partial angles of C
    angle1 = math.asin((c/2)*math.sin(B)/h)
    angle2 = math.asin((c/2)*math.sin(A)/h)
    # using cos to get x displacement
    x1 = a * math.cos(math.pi/2 - angle1)
    x2 = b * math.cos(math.pi/2 - angle2)
    # x1 == x2 because the triangle hangs such that
    # the median splits c into halves
    total += x1 + x2


print(total)
