import sys


for line in sys.stdin:
    if line.strip() == '0':
        break
    s, l = line.split()
    type1 = {s}
    type2 = set()
    type3 = set()

    for i in range(len(s)):
        type2.add(s[:i]+s[i+1:])
        for c in {'A', 'C', 'G', 'T'}:
            type3.add(s[:i] + c + s[i:])
    for c in {'A', 'C', 'G', 'T'}:
        type3.add(s+c)
    n = len(s)
    t1 = 0
    t2 = 0 
    t3 = 0
    for i in range(0, len(l)-n+2):
        for s in type2:
            if l[i:i+n-1] == s:
                t2 += 1
    for i in range(0, len(l)-n+1):
        for s in type1:
            if l[i:i+n] == s:
                t1 += 1
    for i in range(0, len(l)-n):
        for s in type3:
            if l[i:i+n+1] == s:
                t3 += 1
    print(t1, t2, t3)

