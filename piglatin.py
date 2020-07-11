import sys


def pig_latin(w):
    vowel = {'a', 'e', 'i', 'o', 'u', 'y'}
    i = 0
    while i < len(w):
        if w[i] in vowel:
            break
        i += 1
    if i == 0:
        res = w + 'yay'
    else:
        res = w[i:] + w[:i] + 'ay'
    return res


for line in sys.stdin:
    words = line.split()
    res = []
    for w in words:
        res.append(pig_latin(w))
    print(' '.join(res))
