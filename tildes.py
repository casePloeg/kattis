# union find simulation
# path compression should bring it down
# to O(1) amortized time per query

n, q = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for i in range(n)]
size = [1 for i in range(n)]

def find(a):
    if parent[a] == a:
        return a
    else:
        p = find(parent[a])
        # path compression
        parent[a] = p
        return p

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    # check that the two nodes aren't already merged
    if a_root != b_root:
        if rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
            size[a_root] += size[b_root]
        elif rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
            size[b_root] += size[a_root]
        else:
            parent[b_root] = a_root
            size[a_root] += size[b_root]
            rank[a_root] += 1

res = []
for _ in range(q):
    query = input().split()
    if query[0] == 's':
        a = int(query[1])
        a_root = find(a-1)
        res.append(str(size[a_root]))
    else:
        a, b = map(int, query[1:])
        union(a-1, b-1)
# fast io, print everything after, not one at a time
print('\n'.join(res))
