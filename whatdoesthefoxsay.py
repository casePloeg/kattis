t = int(input())
for _ in range(t):
    sounds = input().split()
    res = []
    animals = dict()
    line = input().split()
    while len(line) == 3:
        a, goes, s = line
        animals[s] = a
        line = input().split()
    for s in sounds:
        if s not in animals:
            res.append(s)
    print(' '.join(res))

