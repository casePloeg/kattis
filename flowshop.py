n, m = map(int, input().split())
swathers = [list(map(int, input().split())) for _ in range(n)]
swathers = [[0 for _ in range(m)]] + swathers
res = []
for i in range(1, n+1):
    last = 0
    for j in range(m):
        swathers[i][j] += max(last, swathers[i-1][j])
        last = swathers[i][j]
    res.append(swathers[i][-1])
print(' '.join([str(x) for x in res]))
