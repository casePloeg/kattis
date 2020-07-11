import math
import heapq


s = tuple(map(float, input().split()))
t = tuple(map(float, input().split()))
n = int(input())
nodes = []
for i in range(n):
    u = tuple(map(float, input().split()))
    nodes.append(u)
nodes.append(t)

q = [(0, s, (s,))]
time = dict()
time[s] = 0
while len(q) > 0:
    d, u, path = heapq.heappop(q)
    if u == t:
        print(d)
        break
    for v in nodes:
        x1, y1 = u
        x2, y2 = v

        if u == s:
            new_d = d + math.hypot(x1-x2, y1-y2) / 5
        else:
            total = math.hypot(x1-x2, y1-y2)
            run = abs(total - 50) 
            new_d = d + 2 + run / 5
        if v not in time or new_d <= time[v]:
            time[v] = new_d
            heapq.heappush(q, (new_d, v, path + (v,)))



