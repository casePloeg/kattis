n = int(input())
for i in range(n):
    p, r, f = map(int, input().split())
    years = 0
    while p <= f:
        years += 1
        p *= r

    print(years)