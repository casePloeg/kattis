import sys

for line in sys.stdin:
    grid = []
    end = 0
    while len(line.strip()) != 0:
        grid.append(list(line.strip()))
        line = sys.stdin.readline()
    size = len(grid[0])
    sorted_grid = []
    for row in grid:
        count = 0
        for i in row:
            if i == '*':
                count += 1
        new_row = '.' * (size - end - count) + '*' * count + '.' * (max(end - count, 0)) 
        new_row += '.' * (size - len(new_row))
        end += count
        sorted_grid.append(new_row)
    print('\n'.join(sorted_grid))
    print()
