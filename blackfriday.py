n = int(input())
rolls = list(map(int, input().split()))
unique = dict() 
seen = set()
for i, r in enumerate(rolls):
    if r not in unique and r not in seen:
        unique[r] = i + 1 
        seen.add(r)
    elif r in unique and r in seen: 
        unique.pop(r)
if len(unique) > 0:
    print(unique[max(unique)])
else:
    print('none')
