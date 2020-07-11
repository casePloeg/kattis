key = input().strip().upper()
msg = input().strip().upper()

grid = ['' for x in range(25)]

seen = set()
alpha = [chr(ord('A') + i) for i in range(27)]
a = 0
k = 0
for i in range(25):
    found = False
    while k < len(key):
        if key[k] != ' ' and key[k] not in seen:
            grid[i] = key[k]
            seen.add(key[k])
            k += 1
            found = True
            break
        k += 1
    if not found:
        while a < 27:
            if alpha[a] != 'Q' and alpha[a] not in seen:
                grid[i] = alpha[a]
                seen.add(alpha[a])
                a += 1
                break
            a += 1

res = []
msg = msg.split()
chars = []
for m in msg:
    chars.extend(list(m))
msg = chars

i = 0
while i < len(msg):
    if i == (len(msg) - 1):
        msg = msg[:i+1] + ['X'] + msg[i+1:]
        i -= 2
    else:
        a, b = grid.index(msg[i]), grid.index(msg[i+1])
        if a == b or i == (len(msg) - 1):
            msg = msg[:i+1] + ['X'] + msg[i+1:]
            i -= 2
        elif a // 5 == b // 5:
            res.append(grid[(a//5)*5 + ((a%5) + 1)%5])
            res.append(grid[(b//5)*5 + ((b%5) + 1)%5])
        elif a % 5 == b % 5:
            res.append(grid[(a%5) + (((a//5) + 1)%5)*5])
            res.append(grid[(b%5) + (((b//5) + 1)%5)*5])
        else:
            res.append(grid[(b%5) + (a//5)*5])
            res.append(grid[(a%5) + (b//5)*5])

    i += 2

print(''.join(res))


