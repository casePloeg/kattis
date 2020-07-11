n, V = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]
delta = -V
for box in boxes:
    l, w, h = box
    d = (l*w*h) - V
    delta = max(delta, d)
print(delta)

