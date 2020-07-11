from collections import deque


n = int(input())
grid = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'K':
            k_i, k_j = i, j
            break
visited = [[0 for x in range(n)] for y in range(n)]

# time complexity is number of configs (n^2) multiplied by
# work per configs (iterate through 8 deltas)
def k_jumps(i, j):
    q = deque()
    q.append((0, i, j))
    visited[i][j] = 1
    valid = False
    while len(q) > 0:
        d, i, j = q.popleft()
        if (i,j) == (0,0):
            print(d)
            valid = True
            break

        deltas = {(-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (2, 1), (2, -1), (-1, -2)} 
        for delta in deltas:
            di, dj = delta
            if 0 <= i + di < n and 0 <= j + dj < n and visited[i+di][j+dj] == 0 and grid[i+di][j+dj] != '#':
                visited[i+di][j+dj] = 1
                q.append((d+1, i+di, j+dj))
    if not valid:
        print(-1)
            
k_jumps(k_i, k_j)
