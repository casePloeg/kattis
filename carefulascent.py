x, y = map(int, input().split())
n = int(input())
sheilds = [list(map(float, input().split())) for _ in range(n)]
delta_y = y
for s in sheilds:
    l, u, f = s
    delta_y -= (u - l)
    delta_y += (u - l) * f
print(x/delta_y)

