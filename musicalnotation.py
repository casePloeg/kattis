n = int(input())
notes = input().split()
i = 0
order = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

res = [[] for _ in range(len(order))]
for j, n in enumerate(notes):
    for i in range(len(order)): 
        mark = ' '
        a = 1
        if len(n) > 1:
            a = int(n[1:])
        if order[i] in {'F', 'D', 'B', 'g', 'e', 'a'}:
            mark = '-'
        if n[0] == order[i]:
            if j == 0:
                res[i].append('*' * a)
            else:
                res[i].append(mark + '*' * a)
        else:
            if j == 0:
                res[i].append(mark * (a))
            else:
                res[i].append(mark * (a+1))
length = max(map(len, res))
for i in range(len(res)):
    res[i] = [(order[i] + ': ')] + res[i]
    while len(res[i]) < length:
        mark = ' '
        if order[i] in {'F', 'D', 'B', 'g', 'e', 'a'}:
            mark = '-'
        res[i] = res[i] + mark
print('\n'.join([''.join(x) for x in res]))
