n, m = map(int, input().split())
grid = [list(input()) for x in range(n)]
odd = False
for i in range(n):
    odd = not odd
    skip = False
    for j in range(m):
        need_store = ((i == 0 or grid[i-1][j] == '#') and 
                        (i == n-1 or grid[i+1][j] == '#') and 
                            (j == 0 or grid[i][j-1] == '#') and 
                                (j == m -1 or grid[i][j+1] == '#'))
        if (j % 2 == odd or need_store)  and grid[i][j] != '#':
            grid[i][j] = 'E'
print('\n'.join([''.join(x) for x in grid]))
