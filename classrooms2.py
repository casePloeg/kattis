import heapq
# use disjoint sets instead of a queue to be optimal
n, k = map(int, input().split())

invs = []
for i in range(n):
    # s, f = map(int, input().split())

    invs.append([int(x) for x in input().split()])

intervals = [[] for i in range(k)]
# sort by start time
invs.sort(key=lambda a: (a[1], a[0]), reverse=True)



total = 0
i = n - 1

h = []
for f in range(k):
    h.append((0, f))
while i > -1:
    added = False
    removed = []
    best_index = -1
    best_finish = -1
    while(len(h) > 0):
        smallest = heapq.heappop(h)
        removed.append(smallest)
        if smallest[0] < invs[i][0]:
            best_index = smallest[1]
            best_finish = smallest[0]
        else:
            break
    if best_index > -1:
        added = True
        heapq.heappush(h, (invs[i][1], best_index))
    for r in range(len(removed)):
        if removed[r] != (best_finish, best_index):
            heapq.heappush(h, removed[r])

    # best_interval = (-1, 0)
    # for j in range(k):
    #     if len(intervals[j]) > 0:
    #         if best_interval[1] < intervals[j][-1][1] and intervals[j][-1][1] < invs[i][0]:
    #             best_interval = (j, intervals[j][-1][1])
    #             added = True
    #     else:
    #         if best_interval[1] <= 0:
    #             best_interval = (j, 0)
    #             added = True
    if added:
        intervals[best_index].append(invs[i])
        invs.pop(i)
        total += 1
    i -= 1


print(total)