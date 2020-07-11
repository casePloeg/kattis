import math
import heapq


m, n = map(int, input().split())
vault = [list(map(int, input().split())) for y in range(m)]

# find shortest path from 0,0 to m-1,n-1 where length of
# path is defined as max signed difference between adjacent
# positions

dist = dict()
# heuristic dijkstra, when found end, return d
def dijkstra(s, t):
    q = [(0, s)]
    while len(q) > 0:
        d, v = heapq.heappop(q)
        if v == t:
            print(d)
            break
        i, j = v
        deltas = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        for delta in deltas:
            di, dj = delta
            if 0 <= i + di < m and 0 <= j + dj < n: 
                new_d = max(d, vault[i+di][j+dj] - vault[i][j])
                u = (i+di,j+dj)
                if u not in dist or new_d < dist[u]:
                    dist[u] = new_d
                    heapq.heappush(q, (new_d, u))


dijkstra((0,0), (m-1,n-1))
    
