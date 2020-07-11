from collections import deque


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
visited = set()
count = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L' and (i,j) not in visited:
            count += 1
            q = deque()
            q.append((i,j))
            while len(q) > 0:
                x, y = q.popleft()
                visited.add((x,y))
                if x > 0 and (x-1,y) not in visited and grid[x-1][y] != 'W':
                    q.append((x-1,y))
                    visited.add((x-1,y))
                if x < r-1  and (x+1,y) not in visited and grid[x+1][y] != 'W':
                    q.append((x+1,y))
                    visited.add((x+1,y))
                if y < c-1  and (x,y+1) not in visited and grid[x][y+1] != 'W':
                    q.append((x,y+1))
                    visited.add((x,y+1))
                if y > 0  and (x,y-1) not in visited and grid[x][y-1] != 'W':
                    q.append((x,y-1))
                    visited.add((x,y-1))
print(count)

