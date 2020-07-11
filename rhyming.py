s = input().strip()
e = int(input())
endings = []
for i in range(e):
    endings.append(set(input().split()))
p = int(input())
for i in range(p):
    line = input().split()
    r = False
    for j in range(e):
        for k in range(len(s)): 
            for k2 in range(len(line[-1])):
                if s[-k:] in endings[j] and line[-1][-k2:] in endings[j]:
                    r = True
    if r:
        print('YES')
    else:
        print('NO')
