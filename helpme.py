white = []
black = []
for i in range(8):
    input()
    line = input().split('|')
    line = line[1:-1]
    if i == 7:
        input()
    for j, sq in enumerate(line):
        if sq[1].isupper():
            white.append((sq[1], i, j))
        elif sq[1].islower():
            black.append((sq[1], i, j))

w = []
b = []

for p in white:
    a, i, j = p
    res = a + chr(ord('a') + j) + str(8 - i)
    w.append(res)
for p in black:
    a, i, j = p
    res = a + chr(ord('a') + j) + str(8 - i)
    b.append(res)
w.sort(key=lambda x: ('KQRBNP'.find(x[0]), x[2], x[1]))
b.sort(key=lambda x: ('kqrbnp'.find(x[0]), 8 - int(x[2]), x[1]))
w = map(lambda x: x[1:] if x[0].lower() == 'p' else x, w)
b = map(lambda x: x[1:] if x[0].lower() == 'p' else x[0].upper() + x[1:], b)

print('White:', ','.join(w))
print('Black:', ','.join(b))



