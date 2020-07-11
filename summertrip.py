events = list(input())
count = 0


for i, s in enumerate(events):
    seen = set()
    for j, t in enumerate(events[i+1:]):
        if t != s and t not in seen:
            count += 1
            seen.add(t)
        elif t == s:
            break
print(count)
