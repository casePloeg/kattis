t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    months = list(map(int, input().split()))
    cur = 6
    # friday is 4
    total = 0
    for m in months:
        for i in range(m):
            if i == 12 and cur == 4:
                total += 1
            cur += 1
            cur %= 7
    print(total)

