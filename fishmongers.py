n, m = map(int, input().split())
fish = [int(x) for x in input().split()]
mongers = []
for i in range(m):
    mongers.append([int(x) for x in input().split()])

fish.sort(reverse=True)
mongers.sort(reverse=True, key=lambda a: a[1])

money = 0
cur_monger = 0
fish_count = 0
i = 0
while i < n and cur_monger < m:
    # can still use this guy
    if fish_count < mongers[cur_monger][0]:
        money += mongers[cur_monger][1] * fish[i]
        i += 1
        fish_count += 1
    else:
        # move to next guy
        cur_monger += 1
        fish_count = 0

print(money)