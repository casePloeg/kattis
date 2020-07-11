n = int(input())
boils = [list(map(int, input().split())) for _ in range(n)]
possible = set() 
for i in range(boils[0][0], boils[0][1]+1):
    possible.add(i)
for j in range(1, n):
    p2 = set()
    for i in range(boils[j][0], boils[j][1]+1):
        p2.add(i)
    possible = possible.intersection(p2)
if len(possible) > 0:
    print('gunilla has a point')
else:
    print('edward is right')
        

