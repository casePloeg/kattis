t = int(input())
for _ in range(t):
    input()
    n = int(input())
    total = 0
    for i in range(n):
        total += int(input()) % n 
    if total % n == 0:
        print('YES')
    else:
        print('NO')
