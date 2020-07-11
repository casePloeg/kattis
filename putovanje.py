n, c = map(int, input().split())
fruits = list(map(int, input().split()))
eaten = 0
for i in range(n):
    e = 0
    w = 0
    for j in range(i, n):
        
        if w + fruits[j] <= c:
            w += fruits[j]
            e += 1
    eaten = max(eaten, e)
print(eaten)

