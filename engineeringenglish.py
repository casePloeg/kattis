import sys

seen = set()
res = []
for line in sys.stdin:
    line = line.split()
    for w in line:
        if w.lower() not in seen:
            res.append(w)
            seen.add(w.lower())
        else:
            res.append('.')
print(' '.join(res))
