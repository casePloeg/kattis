cases = int(input())
for z in range(cases):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        line = [int(_) for _ in input()]
        grid.append(line)
    columns = list(zip(*grid))
    a = ''
    for i in range(m):
        if sum(columns[i]) <= n // 2:
            a += '0'
        else:
            a += '1'
    print(a)
