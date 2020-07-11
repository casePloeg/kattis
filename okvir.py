m, n = map(int, input().split())
u, l, r, d = map(int, input().split())
words = [input().strip() for _ in range(m)]
h = m + u + d
w = n + l + r
res = [['' for x in range(w)] for y in range(h)]
for i in range(h):
    for j in range(w):
        if u <= i < m+u and l <= j < n+l:
            res[i][j] = words[i-u][j-l]
        else:
            if (i%2) ^ (j%2):
                res[i][j] = '.'
            else:
                res[i][j] = '#'
print('\n'.join([''.join(x) for x in res]))

