r, b = map(int, input().split())
n = r+b

for i in range(1, n):
    if n % i == 0:
        x, y = i, n // i
        if (x-2) * (y-2) == b:
            print(max(x,y), min(x,y))
            break



