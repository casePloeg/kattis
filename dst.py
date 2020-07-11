n = int(input())

for _ in range(n):
    roll, d, h, m = input().split()
    d, h, m = map(int, [d, h, m])
    if roll == 'B':
        m -= d
    elif roll == 'F':
        m += d
    h += m // 60
    m %= 60
    h %= 24
    print(h, m)

