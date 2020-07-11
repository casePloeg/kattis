import sys
from collections import defaultdict


i = 1
owes = defaultdict(int)
entered = dict()

for line in sys.stdin:
    line = line.strip()
    if line == 'OPEN':
        owes = defaultdict(int)
        entered = dict()
    elif line == 'CLOSE':
        print('Day ' + str(i))
        for k, v in sorted(owes.items()):
            print(k, '$' + '{:0.2f}'.format(v/10))
        print()
        i += 1
    else:
        e, n, amt = line.split()
        if e == 'ENTER':
            entered[n] = int(amt)
        elif e == 'EXIT':
            owes[n] += int(amt) - entered[n]

