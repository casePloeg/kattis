from collections import deque


w, h = map(int, input().split())
grid = [list(input()) for _ in range(h)]
# find start
s_i = -1
s_j = -1 
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'P': 
            s_i = i
            s_j = j
            break

count = 0
if s_i != -1:
    visited = set()
    q = deque()
    visited.add((s_i, s_j))
    q.append((s_i, s_j))
    while len(q) > 0:
        i, j = q.popleft()
        if grid[i][j] == 'G':
            count += 1
        deltas = {(1,0), (0,1), (-1,0), (0,-1)}
        options = []
        trap = False
        for d in deltas:
            di, dj = d
            if 1 <= i + di <= h-2 and 1 <= j + dj <= w-2:
                if grid[di+i][dj+j] == 'T':
                    trap = True
                if grid[i+di][j+dj] != '#' and (i+di, j+dj) not in visited:
                    options.append((i+di, j+dj))
        if not trap:
            for o in options:
                visited.add(o)
                q.append(o)
print(count)

