n = int(input())
for _ in range(n):
    coords = list(map(int, input().split()))
    m = coords.pop(0) * 2
    x = [coords[i] for i in range(0, m, 2)]
    y = [coords[i] for i in range(1, m, 2)]
    x.append(x[0])
    y.append(y[0])
    se = 0
    for i in range(len(x)-1):
        se += x[i] * y[i+1]
    sw = 0
    for i in range(len(x)-1):
        sw += x[i+1] * y[i]
    print((se-sw)*(1/2))

