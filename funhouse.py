w, l = map(int, input().split())
n = 1
while w + l != 0:
    room = [list(input()) for _ in range(l)]
    # find start
    s_i = 0
    s_j = 0
    for i in range(l):
        for j in range(w):
            if room[i][j] == '*':
                s_i, s_j = i, j
                break
    # find start direction
    direction = 0
    if s_i == 0:
        direction = 2
    elif s_i == l-1:
        direction = 0
    elif s_j == 0:
        direction = 1
    elif s_j == w-1:
        direction = 3
    # move
    c_i, c_j = s_i, s_j
    while room[c_i][c_j] != 'x':
        if direction == 0:
            c_i -= 1
        elif direction == 1:
            c_j += 1
        elif direction == 2:
            c_i += 1
        elif direction == 3:
            c_j -= 1

        if room[c_i][c_j] == '/':
            if direction == 1:
                direction = 0
            elif direction == 0:
                direction = 1
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2

        if room[c_i][c_j] == '\\':
            if direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            elif direction == 0:
                direction = 3
            elif direction == 3:
                direction = 0
    room[c_i][c_j] = '&'
    print('HOUSE ' + str(n))
    print('\n'.join([''.join(line) for line in room]))
    n += 1

    w, l = map(int, input().split())

