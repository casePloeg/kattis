from collections import defaultdict, deque


def connected_components(adj_list):
    visited = set()
    cc = 0
    for v, neighbours in adj_list.items():
        if v not in visited:
            cc += 1
            q = deque()
            q.append(v)
            while len(q) > 0:
                u = q.popleft()
                visited.add(u)
                for n in adj_list[u]:
                    if n not in visited:
                        q.append(n)
    return cc



n = int(input()) # number of cities
for _ in range(n):
    m = int(input())
    r = int(input())
    adj_list = defaultdict(list)
    for i in range(m):
        adj_list[i] = []
    for i in range(r):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    print(connected_components(adj_list) - 1)
