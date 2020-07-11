from collections import defaultdict


m, n = map(int, input().split())
value = defaultdict(int)
for _ in range(m):
    w, v = input().split()
    value[w] = int(v)
for _ in range(n):
    total = 0
    flag = True
    while flag:
        line = input().split()
        for w in line:
            if w == '.':
                flag = False
                break
            total += value[w]
    print(total)

