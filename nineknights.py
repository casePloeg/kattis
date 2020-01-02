def knight_valid(grid, row, col):
    valid = True
    # primary direction: sideways
    # down, right
    if row + 2 < 5 and col + 1 < 5 and grid[row + 2][col + 1] == 'k':
        valid = False
    # down, left
    if row + 2 < 5 and col - 1 > 0 and grid[row + 2][col - 1] == 'k':
        valid = False
        # up, right
    if row - 2 > 0 and col + 1 < 5 and grid[row - 2][col + 1] == 'k':
        valid = False
        # up, left
    if row - 2 > 0 and col - 1 > 0 and grid[row - 2][col - 1] == 'k':
        valid = False
    # primary direction: vertical
    # down, right
    if row + 1 < 5 and col + 2 < 5 and grid[row + 1][col + 2] == 'k':
        valid = False
        # down, left
    if row + 1 < 5 and col - 2 > 0 and grid[row + 1][col - 2] == 'k':
        valid = False
        # up, right
    if row - 1 > 0 and col + 2 < 5 and grid[row - 1][col + 2] == 'k':
        valid = False
        # up, left
    if row - 1 > 0 and col - 2 > 0 and grid[row - 1][col - 2] == 'k':
        valid = False
    return valid


grid = []
for i in range(5):
    grid.append(input().strip())

knights = 0
for i in range(5):
    for j in range(5):
        if grid[i][j] == 'k':
            knights += 1
            if not knight_valid(grid, i, j):
                print('invalid')
                exit()
if knights == 9:
    print('valid')
else:
    print('invalid')
