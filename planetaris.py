n, a = map(int, input().split())
events = [int(x) for x in input().split()]
events.sort()
i = 0
total = 0
while a >= 0 and i < n:
    if a > events[i]:
        total += 1
        a -= (events[i] + 1)
    else:
        break
    i += 1
print(total)