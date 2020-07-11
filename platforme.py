n = int(input())
pilars = 0
height = [0 for i in range(10001)]
platforms = [tuple(map(int, input().split())) for _ in range(n)]
platforms.sort()
for i in range(n):
    y, x1, x2 = platforms[i]
    pilars += y - height[x1]
    pilars += y - height[x2-1]

    for j in range(x1, x2):
        height[j] = y

print(pilars)


