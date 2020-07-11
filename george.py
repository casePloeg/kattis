from collections import defaultdict
import math
import heapq


def find_shortest(s, t, k, adj_list, g_times, g_int, times):
    # adoptation of dijkstra's shortest path
    # keeping track of current time and comparing wait times
    # compared to finding a different route
    q = [(k, s, None)]
    dist = dict()
    # starting at k time
    dist[s] = k
    for v in adj_list:
        if v != s:
            heapq.heappush(q, (math.inf, v, None))
            dist[v] = math.inf
    while len(q) > 0:
        time, cur, prev = heapq.heappop(q)
        if cur == t:
            return time
        if dist[cur] == time:
            for v in adj_list[cur]:
                alt = time + times[(cur, v)] 
                i = 0
                while i < len(g_times) - 1:
                    # check for blocked
                    if ((g_times[i] <= time < g_times[i+1]) and  
                        ((g_int[i],g_int[i+1]) == (cur,v) or (g_int[i],g_int[i+1]) == (v,cur))):
                        alt += g_times[i+1] - time
                    i += 1
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(q, (alt, v, cur)) 
    return -1


n, m = map(int, input().split())
s, t, k, g = map(int, input().split())
g_int= list(map(int, input().split()))
streets = [list(map(int,input().split())) for i in range(m)]
adj_list = defaultdict(list) 
time = defaultdict(int)
for info in streets:
    a, b, l = info
    adj_list[a].append(b)
    adj_list[b].append(a)
    time[(a,b)] = l
    time[(b,a)] = l
g_times = [0]
for i in range(1, g):
    g_times.append(time[(g_int[i], g_int[i-1])]+g_times[i-1])
print(find_shortest(s, t, k, adj_list, g_times, g_int, time) - k)

