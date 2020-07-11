n, h, v = map(int, input().split())

h = max(n-h, h)
v = max(n-v, v)
print(h*v*4)

