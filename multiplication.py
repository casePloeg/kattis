a, b = map(int, input().split())
while a + b != 0:
    a = list(map(int, list(str(a))))
    b = list(map(int, list(str(b))))
    vals = []
    place_val = [0 for _ in range(len(a) + len(b))]
    for i in range(len(b)):
        vals.append([])
        for j in range(len(a)):
            s = b[i] * a[j]
            vals[i].append(s)
            place_val[len(a)-1-j + len(b)-1-i] += s % 10
            place_val[len(a)-1-j + len(b)-1-i+1] += s // 10

    for i, v in enumerate(place_val):
        if v > 9:
            place_val[i+1] += place_val[i] // 10
            place_val[i] %= 10
    res = [[] for _ in range(len(b) * 3)]
    for i in range(len(b)):
        for j in range(len(a)):
            res[i*3].append(str(vals[i][j]//10) + ' /|')
            res[i*3+1].append(' / |')
            res[i*3+2].append('/ ' + str(vals[i][j]%10) + '|')
    print('+', '-'*((3 * len(a)) + len(a) + 3), '+', sep='')
    print('|   ', '   '.join([str(x) for x in a]), '   |', sep='')
    cur_pv = len(place_val) - 1
    first = True
    for i in range(len(res)):
        if i % 3 == 0:
            print('| +', end='')
            print('+'.join(['---' for _ in range(len(a))]), end='')
            print('+ |')
        print('|',end='')

        if i % 3 == 2: 
            if place_val[cur_pv] != 0:
                first = False
                print(place_val[cur_pv], end='')
            else:
                print(' ', end='')
            cur_pv -= 1
        elif i%3 == 0 and not first:
            print('/', end='')
        else:
            print(' ', end='')

        print('|', end='')
        print(''.join(res[i]), end='')
        if i % 3 == 1:
            print(b[i//3], end='')
        else:
            print(' ', end='')
        print('|')
    print('| +', end='')
    print('+'.join(['---' for _ in range(len(a))]), end='')
    print('+ |')
    tmp = ''
    if first:
        tmp += '|  '
    else:
        tmp += '|/ '
    tmp += ' / '.join([str(x) for x in reversed(place_val[:cur_pv+1])])
    length = ((3 * len(a)) + len(a) + 3)
    tmp += ' ' * (length - len(tmp) + 1)
    tmp += '|'
    print(tmp)
    print('+', '-'*length, '+', sep='')
    a, b = map(int, input().split())

