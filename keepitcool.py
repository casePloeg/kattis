n, m, s, d = map(int, input().split())
slots = list(map(int, input().split()))

slot = 0
res = [0 for _ in range(s)]
while n > 0:
    possible = False 
    summ = 0 
    for i in range(s):
        if res[i] == 0:
            n_summ = sum(slots[:i] + slots[i+1:]) 
            if n_summ >= m and n_summ > summ:
                possible = True
                summ = n_summ
                slot = i
    if possible:
        res[slot] = min(d - slots[slot], n)
        slots[slot] = 0
        n = n - res[slot] 
    else:
        break
if not possible:
    print('impossible')
else:
    print(' '.join([str(x) for x in res]))


