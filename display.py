import sys

nums = [
    ['+-+', '| |', '+ +', '| |', '+-+'],
    ['  +', '  |', '  +', '  |', '  +'],
    ['+-+', '  |', '+-+', '|  ', '+-+'],
    ['+-+', '  |', '+-+', '  |', '+-+'],
    ['+ +', '| |', '+-+', '  |', '  +'],
    ['+-+', '|  ', '+-+', '  |', '+-+'],
    ['+-+', '|  ', '+-+', '| |', '+-+'],
    ['+-+', '  |', '  +', '  |', '  +'],
    ['+-+', '| |', '+-+', '| |', '+-+'],
    ['+-+', '| |', '+-+', '  |', '+-+'],
]

for line in sys.stdin:
    line = line.strip()
    if line == 'end':
        print('end')
        break
    res = [[] for _ in range(7)]
    for n in line:
        if n == ':':
            for j in {0, 1, 3, 5, 6}:
                res[j].append(' ')
            res[2].append('o')
            res[4].append('o')
        else:
            delta = 0
            for i, l in enumerate(nums[int(n)]):
                res[i+delta].append(l[0] + l[1] * 3 + l[2])
                if i in {1, 3}:
                    delta += 1
                    res[i+delta].append(l[0] + l[1] * 3 + l[2])
    print('\n'.join(['  '.join(x) for x in res]))
    print()
    print()
