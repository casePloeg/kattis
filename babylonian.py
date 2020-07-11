n = int(input())
for _ in range(n):
    b = input().split(',')
    b = b[::-1]
    decimal = 0
    for i, num in enumerate(b):
        if num != '':
            decimal += (60 ** i) * int(num)
    print(decimal)
