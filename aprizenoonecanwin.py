n, x = map(int, input().split())
items = [int(x) for x in input().split()]
items.sort()
marked = 1
for i in range(1, n):
    if items[i] + items[i - 1] <= x:
        marked += 1
print(marked)
