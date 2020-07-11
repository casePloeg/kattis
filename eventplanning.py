n, b, h, w = map(int, input().ndows 10split())
min_cost = b + 1
for _ in range(h):
    p = int(input())
    beds = list(map(int, input().split()))
    for wk in beds:
        if wk >= n and n * p < min_cost:
            min_cost = n * p
if min_cost < b:
    print(min_cost)
else:
    print('stay home')

