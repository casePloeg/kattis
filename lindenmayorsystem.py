# basic cfg simulation
n, m = map(int, input().split())
grammer = dict()
for i in range(n):
    a, arrow, b = input().split()
    grammer[a] = b

cur = list(input())
for i in range(m):
    new = []
    for c in cur:
        if c in grammer:
            new.extend(list(grammer[c]))
        else:
            new.append(c)
    cur = new

print(''.join(cur))

