import heapq


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(edge_list, n):
    parent = []
    rank = []
    for i in range(n):
        parent.append(i)
        rank.append(0)
    edges = 0
    while edges < n-1: 
        d, i, j = edge_list.pop() 
        x = find(parent, i)
        y = find(parent, j)
        if x != y:
            edges += 1
            print(i+1, j+1)
            union(parent, rank, x, y)
            
    
n = int(input())
edge_list = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i+1, n):
        edge_list.append((row[j], i, j))

kruskal(sorted(edge_list, reverse=True), n)
