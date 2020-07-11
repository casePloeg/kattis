def smallest(mask):

    size = 0
    board = ''
    for i in range(12):

        if (mask & (1<<i)):
            board += 'o'
            size += 1
        else:
            board += '-'
    for i in range(12):
        if i < 10 and (not(mask & (1<<i))) and (mask & (1<<(i+1))) and (mask & (1<<(i+2))):
            new_mask = (mask & ~(1<<(i+1)))
            new_mask = (new_mask | (1<<(i)))
            new_mask = (new_mask & ~(1<<(i+2)))
            size = min(size, smallest(new_mask))
        if i < 10 and (mask & (1<<i)) and (mask & (1<<(i+1))) and (not (mask & (1<<(i+2)))):
            new_mask = (mask & ~(1<<(i+1)))
            new_mask = (new_mask | (1<<(i+2)))
            new_mask = (new_mask & ~(1<<(i)))
            size = min(size, smallest(new_mask))
    return size


t = int(input())
for _ in range(t):
    board = input().strip()
    n = 1 << 12
    mask = 0
    for i, c in enumerate(board):
        if c == 'o':
            mask = mask | (1<<i)
    print(smallest(mask))

