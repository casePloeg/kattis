import heapq


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
q = [] 
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            heapq.heappush(q, (0, 1, i, j))
dist = dict()
flag = False
while len(q) > 0:
    d, num, i, j = heapq.heappop(q)
    if num == k:
        print(d)
        flag = True
        break
    else:
        for x in range(n):
            for y in range(n):
                if grid[x][y] == num + 1:
                    delta = abs(i-x) + abs(j-y)
                    if (x,y) not in dist or d + delta < dist[(x,y)]:
                        heapq.heappush(q,(d+delta, num+1, x, y))
                        dist[(x,y)] = d + delta

if not flag:
    print(-1)

