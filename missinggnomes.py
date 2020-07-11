m, n = map(int, input().split())
gn = [int(input()) for _ in range(n)]
res = []
gn_set = set(gn)

cur = 0
i = 1
while len(res) < m:
    if i not in gn_set and (cur >= n or i < gn[cur]):
        res.append(str(i))
        i += 1
    elif i in gn_set:
        i += 1
    else:
        res.append(str(gn[cur]))
        cur += 1
print('\n'.join(res))

