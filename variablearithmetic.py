msg = input().strip()
vars = dict()
while msg != '0':
    tokens = msg.split()
    res = []
    n = 0
    if len(tokens) == 3 and tokens[1] == '=':
        vars[tokens[0]] = int(tokens[2])
    else:
        for t in tokens:
            if t.isnumeric():
                n += int(t)
            elif t in vars:
                n += vars[t]
            elif t != '+':
                res.append(t)
        if (n == 0 and len(res) == 0) or n != 0:
            res = [str(n)] + res
        print(' + '.join(res))


    msg = input().strip()

