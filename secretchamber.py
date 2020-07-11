from collections import defaultdict, deque


m, n = map(int, input().split())
adj_matrix = [[0 for x in range(26)] for y in range(26)]
translations = defaultdict(list)
for i in range(m):
    a, b = input().split()
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    adj_matrix[a][b] = 1
path = adj_matrix
for k in range(26):
    for i in range(26):
        for j in range(26):
            path[i][j] = (path[i][j] or (path[i][k] and path[k][j])) 

for i in range(n):
    w1, w2 = map(list, input().split())
    valid = False
    if len(w1) == len(w2):
        valid = True
        for j in range(len(w1)):
            a = ord(w1[j]) - ord('a')
            b = ord(w2[j]) - ord('a')
            if not (path[a][b] or a == b):
                valid = False
                break
    if not valid:
        print('no')
    else:
        print('yes')
                
