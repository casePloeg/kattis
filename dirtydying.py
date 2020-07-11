n, p = map(int, input().split())
dists = list(map(int, input().split()))
dists.sort()
d = 0
cur = 0
for i in range(n):
    d = max(d, p * (i+1) - dists[i] + dists[0])
print(d)
