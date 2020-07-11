n, k = map(int, input().split())
cur = 0
pos = [0]
throws = input().split()
i = 0
while i < len(throws):
    t = throws[i]
    if t.lstrip('-').isnumeric():
        pos.append((pos[-1]+int(t)) % n)
        i += 1
    else:
        t = int(throws[i+1])
        # undo t throws
        for j in range(t):
            pos.pop()
        i += 2
print(pos[-1])
