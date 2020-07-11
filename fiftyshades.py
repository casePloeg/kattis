n = int(input())

total = 0
for i in range(n):
    w = input().lower()
    if 'pink' in w or 'rose' in w:
        total += 1
if total > 0:
    print(total)
else:
    print("I must watch Star Wars with my daughter")

