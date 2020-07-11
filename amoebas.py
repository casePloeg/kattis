def find_cell(i, j, m, n, visited, grid):
    cell = [(i,j)]
    while len(cell) > 0:
        i, j = cell.pop()
        if not visited[i][j] and grid[i][j] == '#':
            if i < m - 1:
                cell.append((i+1, j))
            if i > 0:
                cell.append((i-1, j))
            if i < m - 1 and j < n - 1:
                cell.append((i+1, j+1))
            if i > 0 and j > 0:
                cell.append((i-1, j-1))
            if i > 0 and j < n - 1:
                cell.append((i-1, j+1))
            if i < m - 1 and j > 0:
                cell.append((i+1, j-1))
            if j > 0:
                cell.append((i, j-1))
            if j < n - 1:
                cell.append((i, j+1))
        visited[i][j] = 1


m, n = map(int, input().split())
visited = [[0 for j in range(n)] for i in range(m)]
grid = [list(input()) for i in range(m)]

count = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#' and not visited[i][j]:
            count += 1
            find_cell(i, j, m, n, visited, grid)
print(count)

