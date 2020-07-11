n = int(input())
for _ in range(n):
    pos = input()
    i = int(pos[1]) - 1
    j = ord(pos[0]) - ord('a')
    board = [[0 for x in range(8)] for y in range(8)]
    cur = [(i,j,0)]
    places  = []
    max_d = -1
    while len(cur) > 0:
        i, j, d = cur.pop(0)
        if d > max_d:
            max_d = d
            places = [chr(j+ord('a'))+str(i+1)] 
        elif d == max_d:
            places.append(chr(j+ord('a'))+str(i+1)) 
        new_i = i-2 
        new_j = j-1 
        new_d = d+1
        if i - 2 >= 0 and j - 1 >= 0 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i-2 
        new_j = j+1 
        new_d = d+1
        if i - 2 >= 0 and j + 1 < 8 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i-1 
        new_j = j-2 
        new_d = d+1
        if i - 1 >= 0 and j - 2 >= 0 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i-1 
        new_j = j+2 
        new_d = d+1
        if i - 1 >= 0 and j + 2 < 8 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i+2 
        new_j = j-1 
        new_d = d+1
        if i + 2 < 8 and j - 1 >= 0 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i+2 
        new_j = j+1 
        new_d = d+1
        if i + 2 < 8 and j + 1 < 8 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i+1 
        new_j = j-2 
        new_d = d+1
        if i + 1 < 8 and j - 2 >= 0 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        new_i = i+1 
        new_j = j+2 
        new_d = d+1
        if i + 1 < 8 and j + 2 < 8 and board[new_i][new_j] != 1:
            board[new_i][new_j] = 1
            cur.append((new_i,new_j,new_d))
        board[i][j] = 1
    print(str(max_d),' '.join(sorted(places, key=lambda x: (x[1], 26 - ord(x[0])), reverse=True)))
