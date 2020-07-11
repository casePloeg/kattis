t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prizes = [list(map(int, input().split())) for x in range(n)]
    stickers = list(map(int, input().split()))
    s = dict()
    for i, stick in enumerate(stickers):
        s[i+1] = stick

    total = 0
    for p in prizes:
        cost, profit = p[1:-1], p[-1]
        valid = True
        while valid:
            for t in cost:
                if s[t] > 0:
                    s[t] -= 1
                else:
                    valid = False
            if valid:
                total += profit
    print(total)

