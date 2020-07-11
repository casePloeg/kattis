n = int(input())
board = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    line = input()
    for j, c  in enumerate(line):
        if c == 'W':
            board[i][j] = 1
valid = True
for i in range(n):
    consec = 0
    w = 0
    cur = -1
    for j in range(n):
        if board[i][j] != cur:
            consec = 1
            cur = board[i][j]
        else:
            consec += 1
        if board[i][j] == 1:
            w += 1
        if consec >= 3:
            valid = False
    if w != n // 2:
        valid = False
for i in range(n):
    consec = 0
    w = 0
    cur = -1
    for j in range(n):
        if board[j][i] != cur:
            consec = 1
            cur = board[j][i]
        else:
            consec += 1
        if board[j][i] == 1:
            w += 1
        if consec >= 3:
            valid = False
    if w != n // 2:
        valid = False

if valid:
    print(1)
else:
    print(0)

