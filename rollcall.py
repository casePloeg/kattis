import sys
from collections import defaultdict

first = defaultdict(int)
names = []
for line in sys.stdin:
    f, l = line.split()
    first[f] += 1
    names.append((f,l))
names.sort(key = lambda x: (x[1], x[0]))
for n in names:
    f, l = n
    if first[f] > 1:
        print(f, l)
    else:
        print(f)

