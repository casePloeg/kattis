hard = ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']

def get_hard(start):
    c = start.lower()
    closest = 27
    const = ''
    for o in hard:
        if abs(ord(c) - ord(o)) < closest:
            closest = abs(ord(c) - ord(o)) 
            const = o

    return const

def get_ending(c):
    ending = ['a', 'o', 'u']
    closest = 27
    v = ''
    for e in ending:
        if abs(ord(c) - ord(e)) < closest:
            closest = abs(ord(c) - ord(e))
            v = e
    return v + 'h'

msg = input().split()
res = []
for w in msg:
    sy = w.split('-')
    const = get_hard(sy[0][0])
    s = list(sy[0])
    if s[0].isupper():
        s[0] = const.upper()
    else:
        s[0] = const
    sy[0] = ''.join(s)
    for i, s in enumerate(sy[1:]):
        s = list(s)
        for j, c in enumerate(s):
            if c in hard:
                s[j] = const
        sy[i+1] = ''.join(s)
    w = ''.join(sy)
    if w[-1].lower() in hard:
        w += get_ending(w[-1].lower())
    res.append(w)
print(' '.join(res))


