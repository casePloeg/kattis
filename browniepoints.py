n = int(input())
while n != 0:
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    s_i, s_j = points[n//2]
    stan = 0
    ollie = 0
    for p in points:
        i, j = p
        if i > s_i and j > s_j:
            stan += 1
        elif i > s_i and j < s_j:
            ollie += 1
        elif i < s_i and j > s_j:
            ollie += 1
        elif i < s_i and j < s_j:
            stan += 1
    print(stan, ollie)
    n = int(input())

