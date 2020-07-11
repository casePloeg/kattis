import math


odds = [[[[0 for a in range(7)] for b in range(7)] for c in range(7)] for d in range(7)]

for a in range(7):
    for b in range(a, 7):
        for c in range(7):
            for d in range(c, 7):
                if (a,b) == (1,2) and (c,d) != (1,2):
                    odds[a][b][c][d] = 1
                    odds[b][a][c][d] = 1
                    odds[a][b][d][c] = 1
                    odds[b][a][d][c] = 1
                elif a == b and (c,d) != (1,2) and (c != d or a > c):
                    odds[a][b][c][d] = 1
                    odds[b][a][c][d] = 1
                    odds[a][b][d][c] = 1
                    odds[b][a][d][c] = 1
                elif (c,d) != (1,2) and (a != b) and (c != d) and (b,a) > (d,c):
                    odds[a][b][c][d] = 1
                    odds[b][a][c][d] = 1
                    odds[a][b][d][c] = 1
                    odds[b][a][d][c] = 1

s0, s1, r0, r1 = input().split()
while s0 != '0':
    win = 0
    lose = 0
    if s0 == '*':
        s0 = [i for i in range(1,7)]
    else:
        s0 = [int(s0)]
    if s1 == '*':
        s1 = [i for i in range(1,7)]
    else:
        s1 = [int(s1)]
    if r0 == '*':
        r0 = [i for i in range(1,7)]
    else:
        r0 = [int(r0)]
    if r1 == '*':
        r1 = [i for i in range(1,7)]
    else:
        r1 = [int(r1)]
    for a in s0:
        for b in s1:
            for c in r0:
                for d in r1:
                    if odds[a][b][c][d]:
                        win += 1
                    else:
                        lose += 1
    g = math.gcd(win, win+lose)
    if win == 0: 
        print(0)
    elif lose == 0:
        print(1)
    else:
        print(win//g, '/', (win+lose)//g, sep='')

    s0, s1, r0, r1 = input().split()
