n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    b = (s - d) // 2
    a = s - b
    if (s - d) % 2 != 0 or (s - d) < 0:
        print('impossible')
    else:
        print(a, b)
