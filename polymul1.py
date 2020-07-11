t = int(input())
for _ in range(t):
    n1 = int(input())
    p1 = list(map(int, input().split()))
    n2 = int(input())
    p2 = list(map(int, input().split()))
    p3 = [0 for i in range(n1 + n2 + 2)]
    for i in range(n1+1):
        for j in range(n2+1):
            p3[i+j] += p1[i]*p2[j]
    d = 0
    for i in range(len(p3)):
        if p3[i] != 0:
            d = i
    print(d)
    print(' '.join([str(x) for x in p3[:d+1]])) 

