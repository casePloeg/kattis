white = input().split()
if len(white) > 1:
    white = white[1].split(',')
else:
    white = []
black = input().split()
if len(black) > 1:
    black = black[1].split(',')
else:
    black = []
board = [['' for _ in range(8)] for _ in range(8)]

for p in white:
    i = int(p[-1]) - 1
    j = int(ord(p[-2]) - ord('a'))
    if len(p) == 2:
        board[i][j] = 'P'
    else:
        board[i][j] = p[0]

for p in black:
    i = int(p[-1]) - 1
    j = int(ord(p[-2]) - ord('a'))
    if len(p) == 2:
        board[i][j] = 'p'
    else:
        board[i][j] = p[0].lower()
board = board[::-1]
for i in range(8): 
    print('+---' * 8, end='+\n')
    for j in range(8):
        print('|', end='')
        c = ':' if (j % 2) ^ (i % 2) else '.'
        if board[i][j] == '':
            print(c * 3, end='')
        else:
            print(c + board[i][j] + c, end='')
    print('|')
print('+---' * 8, end='+\n')

