t = int(input())
for _ in range(t):
    n = int(input())
    throws = [tuple(map(int, input().split())) for x in range(n)]
    score = 0
    for throw in throws:
        x, y = throw
        for p in reversed(range(1, 11)):
            if x**2 + y**2 <= (20 * (11 - p))**2:
                score += p
                break
    print(score)
