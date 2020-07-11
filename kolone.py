n1, n2 = map(int, input().split())
l1 = list(input())
l2 = list(input()) 
right = set(l1)
left = set(l2)
res = []
l1 = l1[::-1]
res.extend(l1)
res.extend(l2)
t = int(input())
for i in range(t):
    j = 0
    while j < (n1+n2-1):
        if res[j] in right and res[j+1] in left:
            res[j], res[j+1] = res[j+1], res[j] 
            j += 2
        else:
            j += 1

print(''.join(res))
