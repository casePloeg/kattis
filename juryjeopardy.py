t = int(input())
print(t)
for _ in range(t):
    top = 0
    bottom = 0
    w = 0
    moves = list(input())
    i, j = 0, 0
    d = 0
    for m in moves:
        if m == 'R':
            d += 1
        if m == 'L':
            d -= 1
        if m == 'B':
            d += 2
        d %= 4
        if d == 0:
            i, j = i, j+1
        elif d == 1:
            i, j = i+1, j
        elif d == 2:
            i, j = i, j-1
        elif d == 3:
            i, j = i-1, j
        top = min(top, i)
        bottom = max(bottom, i)
        w = max(j, w)
    h = abs(top) + abs(bottom) + 1
    grid = [['#' for x in range(w+2)] for y in range(h+2)]
    i, j = 0 - top + 1, 0
    d = 0
    for m in moves:
        grid[i][j] = '.'
        if m == 'R':
            d += 1
        if m == 'L':
            d -= 1
        if m == 'B':
            d += 2
        d %= 4
        if d == 0:
            i, j = i, j+1
        elif d == 1:
            i, j = i+1, j
        elif d == 2:
            i, j = i, j-1
        elif d == 3:
            i, j = i-1, j
    print(h+2, w+2)
    print('\n'.join([''.join(x) for x in grid]))
       
