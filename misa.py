r, s = map(int, input().split())
grid = [list(input()) for _ in range(r)]

handshakes = 0
for mi in range(r):
    for mj in range(s):
        og = grid[mi][mj]  
        if og == '.':
            grid[mi][mj] = 'o'
        n = 0
        for i in range(r):
            for j in range(s):
                for d in [(-1,1), (0,1), (1,1), (1,0)]:
                    di, dj = d
                    if 0 <= i + di <= r-1 and 0 <= j + dj <= s-1:
                        if grid[i][j] == 'o' and grid[i+di][j+dj] == 'o':
                            n += 1

        handshakes = max(handshakes, n)
        grid[mi][mj] = og
print(handshakes)
