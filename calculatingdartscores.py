n = int(input())
viable = set()
for i in range(1, 21):
    viable.add(('single', i, 1))
    viable.add(('double', i, 2))
    viable.add(('triple', i, 3))

valid = False
for d1 in viable:
    for d2 in viable:
        for d3 in viable:
            if d1[1]*d1[2] + d2[1]*d2[2] + d3[1]*d3[2] == n:
                valid = True
                a, b, c = d1, d2, d3
        if d1[1]*d1[2] + d2[1]*d2[2] == n:
            valid = True
            a, b, c = d1, d2, -1
    if d1[1]*d1[2] == n:
        valid = True
        a, b, c = d1, -1, -1

if valid:
    print(*a[:2])
    if b != -1:
        print(*b[:2])
    if c != -1:
        print(*c[:2])
else:
    print('impossible')

