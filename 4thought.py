import itertools

m = int(input())
perms = dict()
for p in itertools.permutations('+++---///***', 3):
    e = '4 '
    # need to keep track of actual expression and printable
    # expression due to integer division requirement
    e_ = '4 '
    for op in p:
        e += op
        
        e_ += op
        if op == '/':
            e_ += '/'
        e += ' 4 '
        e_ += ' 4 '
    n = eval(e_)

    e += '= '
    e += str(int(n))
    perms[n] = e

for _ in range(m):
    n = int(input())
    if n in perms:
        print(perms[n])
    else:
        print('no solution')
