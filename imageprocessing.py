h, w, n, m = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(h)]
kernel = [list(map(int, input().split())) for _ in range(n)]
res = [[0 for x in range(w-m+1)] for y in range(h-n+1)]
for j in range(w-m+1):
    for i in range(h-n+1):
        val = 0
        for l in range(m):
            for k in range(n):
                val += image[i+k][j+l] * kernel[n-k-1][m-l-1]
        res[i][j] = val
print('\n'.join([' '.join(x) for x in [[str(x) for x in line] for line in res]]))
