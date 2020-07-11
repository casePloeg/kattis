n, m = map(int, input().split())
while n + m != 0:
    calls = [list(map(int, input().split())) for _ in range(n)]
    for i in range(m):
        s, d = map(int, input().split())
        t = s + d
        total = 0
        for c in calls:
            # call src/dest shouldn't matter bc each
            # operator can only handle one call anyways
            src, dest, st, dur = c
            if s < st + dur and t > st:
                total += 1
        print(total)
    n, m = map(int, input().split())
