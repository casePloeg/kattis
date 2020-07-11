from collections import defaultdict


info = input().split()
n = int(info[0])
code = info[1]
guess = info[2]
taken = [0 for i in range(n)]
r = 0
for i, p in enumerate(code):
    if guess[i] == p:
        r += 1
        taken[i] = 1
colours = defaultdict(int)
for i in range(n):
    if not taken[i]:
        colours[code[i]] += 1
s = 0
for i in range(n):
    if not taken[i]:
        if colours[guess[i]] > 0:
            s += 1
            colours[guess[i]] -= 1

print(r, s)
